from django.shortcuts import render

from dogs import views
from dogs.models import Dog
from accounts.models import User
from matches.views import DogMatch

from introducedog.settings import SECRET_KEY
from django.views import View
from dogs.serializers import DogSerializer
from rest_framework import generics

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
import sklearn
import pandas as pd

class DogColorMatch(APIView):
    def recommend_dog_with_color(self, req):
        colorin = req['color']
        sex = req['sex']
        dog_list = []

        if len(req['pick']) == 0 & len(req['survey']) == 0 :
            dog_list = Dog.objects.all()
        else :
            #사용자의 선택을 기준으로 선호하는 성격을 가진 종을 찾는다.
            breeds = DogMatch.find_breed_list(self, req['pick'])

            #설문조사를 기준으로 size를 찾는다.
            size_qualification_num = DogMatch.check_qualification(self, req['survey'])
            size = size_qualification_num[0]

            #size 1 : 소형견, 2 : 중형견이하, 3 : 대형견 이하        
            #사이즈, 성격의 코사인 유사도가 높은 목록을 result에 저장
            result = DogMatch.recommend_dog(self, size, breeds)

            #리스트에 있는 아이디를 가진 개의 정보를 json형식으로 rere에 추가한후, return
            for dog in result:
                dog_list.append(self.get_object(dog))

        serializer = DogSerializer(dog_list, many=True)
        data = serializer.data
        df = pd.DataFrame(data)

        df = df[['dog_id', 'kind', 'color', 'sex']]

        #성별 조건이 있다면 F, M -> 그조건에 맞는 data만 남긴다.
        if sex == 'F' :
            is_sex = df['sex'] == 'F'
            df = df[is_sex]
        elif sex == 'M':
            is_sex = df['sex'] == 'M'
            df = df[is_sex]

        ## df에 사용자가 입력한 색을 가지는 가상의 개를 만들어서 넣어 코사인 유사도를 구한다.
        df = df.append({'dog_id':'N011', 'kind':'투명', 'color' : str(colorin), 'sex' : sex}, ignore_index=True)
        
        #CountVectorizer
        counter_vector = HashingVectorizer(ngram_range=(1, 3))
        c_vector_color = counter_vector.fit_transform(df['color'])
        color_c_sim = cosine_similarity(c_vector_color, c_vector_color).argsort()[:, ::-1]
        
        target_index = df['N011' == df['dog_id']].index.values
        print(target_index)

        sim_index = color_c_sim[target_index, :30].reshape(-1)
        sim_index = sim_index[sim_index != target_index]
        print(sim_index)

        result = df.iloc[sim_index]
        return result

    #dog_id에 해당하는 dog를 return해준다, 없다면 http404
    def get_object(self, dog_id):
        try:
            return Dog.objects.get(dog_id=dog_id)
        except Dog.DoesNotExist:
            raise Http404
    
    def post(self, request, format=None):
        #해당 컬러와 유사도가 높은 개 목록을 result에 저장
        result = self.recommend_dog_with_color(request.data)
        for col in result['color']:
            print(col)

        #리스트에 있는 아이디를 가진 개의 정보를 json형식으로 rere에 추가한후, return
        rere = []
        for dog in result['dog_id']:
            rere.append(DogSerializer(self.get_object(dog)).data)
        
        return Response(rere)
        # endate오름, age 나이는 내림

class DogColorContainMatch(APIView):
    def recommend_dog_with_color(self, req):
        colorin = req['color']
        sex = req['sex']
        dog_list = []

        if len(req['pick']) == 0 & len(req['survey']) == 0 :
            dog_list = Dog.objects.all()
        else :
            #사용자의 선택을 기준으로 선호하는 성격을 가진 종을 찾는다.
            breeds = DogMatch.find_breed_list(self, req['pick'])

            #설문조사를 기준으로 size를 찾는다.
            size_qualification_num = DogMatch.check_qualification(self, req['survey'])
            size = size_qualification_num[0]

            #size 1 : 소형견, 2 : 중형견이하, 3 : 대형견 이하        
            #사이즈, 성격의 코사인 유사도가 높은 목록을 result에 저장
            result = DogMatch.recommend_dog(self, size, breeds)

            #리스트에 있는 아이디를 가진 개의 정보를 json형식으로 rere에 추가한후, return
            for dog in result:
                dog_list.append(self.get_object(dog))

        #dog_list = Dog.objects.all()
        serializer = DogSerializer(dog_list, many=True)
        data = serializer.data
        df = pd.DataFrame(data)

        df = df[['dog_id', 'kind', 'color', 'sex']]
        #성별 조건이 있다면 F, M -> 그조건에 맞는 data만 남긴다.
        if sex == 'F' :
            is_sex = df['sex'] == 'F'
            df = df[is_sex]
        elif sex == 'M':
            is_sex = df['sex'] == 'M'
            df = df[is_sex]

        #입력된 색을 포함하는 목록을 찾는다.
        contain_list = []
        for now_id, now_color in zip(df['dog_id'], df['color']):
            print(now_color)
            cnt = 0

            for color in colorin:
                print(color)
                if color in now_color:
                    cnt += 1

            contain_list.append((now_id, cnt))

        contain_list.sort(key= lambda node: node[1], reverse=True)
        print(contain_list)
        return contain_list

    #dog_id에 해당하는 dog를 return해준다, 없다면 http404
    def get_object(self, dog_id):
        try:
            return Dog.objects.get(dog_id=dog_id)
        except Dog.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        #해당 컬러와 유사도가 높은 개 목록을 result에 저장
        result = self.recommend_dog_with_color(request.data)

        #리스트에 있는 아이디를 가진 개의 정보를 json형식으로 rere에 추가한후, return
        rere = []
        for dog in result:
            rere.append(DogSerializer(self.get_object(dog[0])).data)
        
        return Response(rere)