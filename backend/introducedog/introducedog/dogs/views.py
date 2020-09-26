import numpy as np
import glob
import os
from keras.models import load_model
#from PIL import Image
from django.shortcuts import get_object_or_404, render

# Create your views here.
import json

from introducedog.settings import SECRET_KEY

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Dog
from accounts.models import User

from dogs.serializers import DogSerializer
from rest_framework import generics

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

'''
class DogList(View):
    def get(self, request):
        print("full Dog List")
        data = Dog.objects.values()
        return JsonResponse({"data": list(data)}, status=200)
'''


class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class DogFilter(View):
    def get(self, request, user_id):
        print(user_id)
        return user_id


class DogDetail(APIView):
    def get_object(self, dog_id):
        try:
            return Dog.objects.get(dog_id=dog_id)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request, dog_id, format=None):
        dog = self.get_object(dog_id)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, dog_id, format=None):
        dog = self.get_object(dog_id)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, dog_id, format=None):
        dog = self.get_object(dog_id)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FindDogByImg(View):
    def post(self, request):

        img = json.loads(request.body)
        image_w = 64
        image_h = 64

        pixels = image_h * image_w * 3

        X = []
        filenames = []
        files = img

        X = np.array(X)
        model = load_model('dog_recog_model.h5')

        prediction = model.predict(X)
        np.set_printoptions(
            formatter={'float': lambda x: "{0:0.3f}".format(x)})
        cnt = 0

        # 이 비교는 그냥 파일들이 있으면 해당 파일과 비교. 카테고리와 함께 비교해서 진행하는 것은 _4 파일.
        for i in prediction:
            pre_ans = i.argmax()  # 예측 레이블
            print(i)
            print(pre_ans)
            pre_ans_str = ''
            if pre_ans == 0:
                pre_ans_str = "포메"
            elif pre_ans == 1:
                pre_ans_str = "말티즈"
            elif pre_ans == 2:
                pre_ans_str = "치와와"
            elif pre_ans == 3:
                pre_ans_str = "토이푸들"
            else:
                pre_ans_str = "골든리트리버"
            if i[0] >= 0.8:
                print("해당 "+filenames[cnt].split("/")
                      [2]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
            if i[1] >= 0.8:
                print("해당 "+filenames[cnt].split("/")
                      [2]+"이미지는 "+pre_ans_str+"으로 추정됩니다.")
            if i[2] >= 0.8:
                print("해당 "+filenames[cnt].split("/")
                      [2]+"이미지는 "+pre_ans_str+"으로 추정됩니다.")
            # print(filenames[cnt].split("/"))
            if i[3] >= 0.8:
                print("해당 "+filenames[cnt].split("/")
                      [2]+"이미지는 "+pre_ans_str+"으로 추정됩니다.")
            if i[4] >= 0.8:
                print("해당 "+filenames[cnt].split("/")
                      [2]+"이미지는 "+pre_ans_str+"으로 추정됩니다.")
            cnt += 1
            # print(i.argmax()) #얘가 레이블 [1. 0. 0.] 이런식으로 되어 있는 것을 숫자로 바꿔주는 것.
            # 즉 얘랑, 나중에 카테고리 데이터 불러와서 카테고리랑 비교를 해서 같으면 맞는거고, 아니면 틀린거로 취급하면 된다.
            # 이걸 한 것은 _4.py에.
            return JsonResponse({"data": pre_ans_str}, status=200)
