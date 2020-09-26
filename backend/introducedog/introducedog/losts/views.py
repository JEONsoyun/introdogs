import numpy as np
import glob
import os
from keras.models import load_model
from PIL import Image
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from io import BytesIO
# Create your views here.
from dogs.models import Dog
from dogs.serializers import DogSerializer

import urllib
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

import json
from skimage import io
import matplotlib.pyplot as plt


class FindDogByImg(View):
    def post(self, request):
        print("findDogByImg")
        data = json.loads(request.body)
        image_w = 64
        image_h = 64

        pixels = image_h * image_w * 3

        X = []
        filenames = []
        model = load_model(
            'C:\\Users\\multicampus\\Desktop\\jin\\s03p23a307\\backend\\introducedog\\introducedog\\losts\\dog_recog_model.h5')
        res = urllib.request.urlopen(data['img_url']).read()
        img = Image.open(BytesIO(res))
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)
        X.append(data)
        X = np.array(X)
        prediction = model.predict(X)
        np.set_printoptions(
            formatter={'float': lambda x: "{0:0.3f}".format(x)})
        cnt = 0
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
            print(pre_ans_str)
            cnt += 1

            dogList = Dog.objects.filter(kind__contains=pre_ans_str).values()
        return JsonResponse({"data": list(dogList)}, status=200)
