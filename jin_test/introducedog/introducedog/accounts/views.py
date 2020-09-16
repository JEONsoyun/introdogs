from django.shortcuts import render

# Create your views here.

import json

from django.views import View
from django.http import JsonResponse

from .models import User

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
            # user_id = data['user_id'],
            user_name = data['user_name'],
            user_email = data['user_email'],
            user_password = data['user_password'],
            user_profile = data['user_profile'],
            match_dog = data['match_dog'],
            same_dog = data['same_dog'],
        ).save()

        return JsonResponse({'message':'회원가입 완료'},status=200)
        # if User.objects.filter(user_email = data['user_email']).exists() == False:
        #     User.objects.create(user_email = data['user_email'], user_password = data['user_password'])
        #     return JsonResponse({"message" : "회원으로 가입되셨습니다."}, status = 200)
            
        # else:
        #    return JsonResponse({"message" : "이미 존재하는 아이디입니다."}, status = 401)
    def get(self, request):
        users = User.objects.values()
        return JsonResponse({"data" : list(users)}, status = 200)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
            
            user_email = data['user_email'],
            user_password = data['user_password']
            
        )
        if User.objects.filter(user_email = data['user_email']).exists() :
            user = User.objects.get(user_email = data['user_email'])
            if user.user_password == data['user_password'] :
                return JsonResponse({'message':f'{user.user_name}님 로그인 성공!'}, status=200)
            else :
                return JsonResponse({'message':'비밀번호가 틀렸어요'},status = 200)

        return JsonResponse({'message':'등록되지 않은 이메일 입니다.'},status=200)
        # if User.objects.filter(user_email = data['user_email'], user_password = data['user_password']).exists() == True :
        #     return JsonResponse({"message": "로그인에 성공하셨습니다."}, status = 200)
        # else:
        #     return JsonResponse({"message" : "아이디나 비밀번호가 일치하지 않습니다."}, status = 401)

    def get(self, request):
        user = User.objects.values()
        return JsonResponse({"list" : list(user)}, status = 200)