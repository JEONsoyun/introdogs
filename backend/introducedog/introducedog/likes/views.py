from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Like
from accounts.models import User

import json

class MakelikeView(View):
    def post(self, request):
        data = json.loads(request.body)
        myuser = User.objects.filter(user_name = request.session.get('username')).values()
        userid = myuser[0]['user_id']
        dog_id = data['dog_id']
        if Like.objects.filter(dog_id = dog_id, user_id =userid).exists(): #이미 있는 좋아요라면
            return JsonResponse({'message': '이미 눌린 좋아요다..'}, status=400)
        else:
            Like(
                dog_id = dog_id,
                user_id = userid,
            ).save()
            return JsonResponse({'message': '좋아요 누르기 성공'}, status=200)
    
    def get(self, request):
        myuser = User.objects.filter(user_name = request.session.get('username')).values()
        # userid = myuser[0]['user_id']
        # like_dog_list = Like.objects.filter(user_id = userid).values()
        # print(like_dog_list)
        ret = []
        for now_user in myuser:
            now_user_id = now_user['user_id']
            like_dog_list = Like.objects.filter(user_id = now_user_id).values()
            # for now_dog in like_dog_list
            #     now_dog_info = 



        return JsonResponse({'message':'테스트다다다'}, status =200)

class DeletelikeView(View):
    def delete(self, request, dog_id):
        myuser = User.objects.filter(user_name = request.session.get('username')).values()
        userid = myuser[0]['user_id']
        if Like.objects.filter(dog_id = dog_id, user_id = userid).exists(): #이미 있을 때만! 삭제하기
            Like.objects.filter(dog_id = dog_id, user_id = userid).delete()
            return JsonResponse({'message':'좋아요 취소.. 되었다! 음하하'}, status =200)
        else:
            return JsonResponse({'message':'뭔가 이상해'}, status=400)
        
