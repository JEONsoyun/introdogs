import numpy as np
import glob
import os
from keras.models import load_model
from PIL import Image
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from io import BytesIO
# Create your views here.
from dogs.models import Dog
from .forms import UploadDocumentForm
import urllib

import json
import logging
from skimage import io
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)


# def FindDogByImg(request):
#     print("findDogByImg")
#     if request.method == 'POST':
#         # Do not forget to add: request.FILES
#         print("post")
#         form = UploadDocumentForm(request.POST, request.FILES)
#         print(form)
#         print(type(form))
#         print(form.__dict__)
#         if form.is_valid():
#             print("이건 되니")
#             img = form['Img']
#             logger.info(img)
#             return JsonResponse({'message': img}, status=200)
#             form.save()
#     return JsonResponse({'message': "에러"}, status=200)

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
        return JsonResponse({"data": pre_ans_str}, status=200)
