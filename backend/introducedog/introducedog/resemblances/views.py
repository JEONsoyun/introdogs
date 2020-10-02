import numpy as np
import glob
import os
from tensorflow.keras.models import load_model
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
import tensorflow as tf


# Create your views here.
class FindDogByImg(View):
    def post(self, request):
        print("findDogByImg")
        # print(os.getcwd())
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        session = tf.Session(config=config)
        print("여기까지 37")
        data = json.loads(request.body)
        print("여기까지 data ")
        image_w = 128
        image_h = 128

        pixels = image_h * image_w * 3
        X = []
        filenames = []
        print('모델 부르기 직전여기까지')
        model = load_model(
            'C:\\Users\\multicampus\\Desktop\\jin\\s03p23a307\\backend\\introducedog\\introducedog\\losts\\dog_recog_vgg150.h5')
        print("모델 불러옴")
        res = urllib.request.urlopen(data['img_url']).read()
        img = Image.open(BytesIO(res))
        print("이미지 불러옴")
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
            elif pre_ans == 4:
                pre_ans_str = "골든리트리버"
            else:
                pre_ans_str = "진도견"
            print(pre_ans_str)
            cnt += 1
            dogList = Dog.objects.filter(kind__contains=pre_ans_str).values()
        return JsonResponse({"data": list(dogList)}, status=200)
