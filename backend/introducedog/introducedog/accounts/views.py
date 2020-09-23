from django.shortcuts import render

# Create your views here.
import json
import bcrypt
import jwt

from introducedog.settings import SECRET_KEY

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import User
from likes.models import Like

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        try :
            if User.objects.filter(user_email = data['user_email']).exists(): # 존재하는 이메일인지 확인
                return JsonResponse({"message" : "이미 존재하는 이메일 입니다."}, status = 400)
            
            #비밀번호 암호화 부분!
            user_password = data['user_password'].encode('utf-8') #바이트 코드로 변환
            password_crypt = bcrypt.hashpw(user_password, bcrypt.gensalt()) #암호화
            password_crypt = password_crypt.decode('utf-8') #다시 utf-8로 변환


            User(
                # user_id = data['user_id'],
                user_name = data['user_name'],
                user_email = data['user_email'],
                user_password = password_crypt,    #암호화된 패스워드 디비에 저장하자!
                user_profile = data['user_profile'],
                match_dog = data['match_dog'],
                same_dog = data['same_dog'],
            ).save()
        
            return JsonResponse({"message" : "회원가입 성공!"}, status = 200)
        except KeyError:
          return JsonResponse({"message":"INVALID_KEYS"}, status = 400)
       

        
    def get(self, request):
        users = User.objects.values()
        return JsonResponse({"data" : list(users)}, status = 200)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        # User(
        #     user_email = data['user_email'],
        #     user_password = data['user_password']
        # )
        try:
            if User.objects.filter(user_email = data['user_email']).exists() :
                user = User.objects.get(user_email = data['user_email'])

                if bcrypt.checkpw(data['user_password'].encode('utf-8'), user.user_password.encode('utf-8')):
                    token = jwt.encode({'user_email' : data['user_email']}, SECRET_KEY, algorithm = "HS256")
                    token = token.decode('utf-8')                          # 유니코드 문자열로 디코딩
                    request.session['username'] = user.user_name
                    # print(request.session.get('username'))
                    return JsonResponse({"token" : token }, status=200)
                else:
                    return HttpResponse(status = 401)

            return HttpResponse(status=400)
        
        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status = 400)
            # if user.user_password == data['user_password'] :
            #     request.session['username'] = user.user_name
            #     # print(request.session.get('username'))
            #     return JsonResponse({'message':f'{user.user_name}님 로그인 성공!'}, status=200)
            # else :
            #     return JsonResponse({'message':'비밀번호가 틀렸어요'},status = 200)

        # return JsonResponse({'message':'등록되지 않은 이메일 입니다.'},status=200)

class TokenCheckView(View):
    def post(self,request):
        data = json.loads(request.body)

        user_token_info = jwt.decode(data['token'], SECRET_KEY, algorithm = 'HS256')

        if User.objects.filter(user_email=user_token_info['user_email']).exists() :
            return HttpResponse(status=200)

        return HttpResponse(status=403)
    
class LogoutView(View):
    def post(self, request):
        # print(request.session.get('username'))
        if request.session['username'] :
            del(request.session['username'])
        
        return JsonResponse({'message': '로그아웃되었습니다.'}, status = 200)

class MypageView(View) :
    def get(self, request):
        myuser = User.objects.filter(user_name = request.session.get('username')).values()
        
        ret = []

        print(f'myuser : {myuser}')
        
        for now_user in myuser:
            now_user_id = now_user['user_id']
            mylike = Like.objects.filter(user_id=now_user_id).values()
            # python list comprehension
            now_user['dog_like_list'] = [now_val['dog_id'] for now_val in mylike if now_val['user_id'] == now_user_id]

            ret.append(now_user)


        print(ret)
        # doglike = Like.objects.filter(user_id = userid).values()
        return JsonResponse({'user':list(myuser)}, status = 200)

class ApicheckView(View):
    def get(self, request):
        if request.session['username'] :
            return JsonResponse({'message': 'true'})
    
