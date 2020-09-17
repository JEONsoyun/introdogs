from django.shortcuts import render

# Create your views here.

import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import User

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        try :
            if User.objects.filter(user_email = data['user_email']).exists(): # 존재하는 이메일인지 확인
                return JsonResponse({"message" : "이미 존재하는 이메일 입니다."}, status = 400)
            
            User(
                # user_id = data['user_id'],
                user_name = data['user_name'],
                user_email = data['user_email'],
                user_password = data['user_password'],
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
        if User.objects.filter(user_email = data['user_email']).exists() :
            user = User.objects.get(user_email = data['user_email'])
            # print(user.user_name)
            if user.user_password == data['user_password'] :
                request.session['username'] = user.user_name
                # print(request.session.get('username'))
                return JsonResponse({'message':f'{user.user_name}님 로그인 성공!'}, status=200)
            else :
                return JsonResponse({'message':'비밀번호가 틀렸어요'},status = 200)

        return JsonResponse({'message':'등록되지 않은 이메일 입니다.'},status=200)

    def get(self, request):
        user = User.objects.values()
        return JsonResponse({"list" : list(user)}, status = 200)
    
class LogoutView(View):
    def post(self, request):
        # print(request.session.get('username'))
        if request.session['username'] :
            del(request.session['username'])
        
        return JsonResponse({'message': '로그아웃되었습니다.'}, status = 200)



