from django.shortcuts import render

from dogs import views
from dogs.models import Dog
from accounts.models import User

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

class DogMatch(APIView):
    def recommend_dog(self, colorin):
        dog_list = Dog.objects.all()
        serializer = DogSerializer(dog_list, many=True)
        data = serializer.data
        df = pd.DataFrame(data)

        df = df[['dog_id', 'kind', 'color']]
        ## df에 사용자가 입력한 색을 가지는 가상의 개를 만들어서 넣어 코사인 유사도를 구한다.
        df = df.append({'dog_id':'N011', 'kind':'투명', 'color' : str(colorin)}, ignore_index=True)
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
        #reqeust에서 넘어온 값에서 color값을 뽑음
        '''
        {"survey" : {
    "q1" : false,
    "q2" : true,
    "q3" : false,
    "q4" : false,
    "q5" : 4,
    "q6" : true,
    "q7" : false,
    "q8" : false,
    "q9" : true,
    "q10" : 2,
    "q11" : 4
}} 
        '''
        data = request.data
        survey = data['survey']

        rere = []

        # 반려동물 입양 자격 미달자를 거르는 과정
        # q1 : 반려동물을 해외 입양 or 외국인 여부
        if survey['q1'] :
            return Response({'qualification' : False, 'list' : rere, 'num' : 1})

        # q2 : 알러지에 대해 충분한 고려 여부
        if not survey['q2']:
            return Response({'qualification' : False, 'list' : rere, 'num' : 2})
        
        # q3 : 강아지가 혼자 지내는 시간 8시간 이상인가
        if survey['q3'] :
            return Response({'qualification' : False, 'list' : rere, 'num' : 3})

        # q4 : 3세 미만의 자녀가 있어요
        if survey['q4'] : 
            return Response({'qualification' : False, 'list' : rere, 'num' : 4})

        # q5 : 반려동물을 기를 곳 여부
        if survey['q5'] != 4 :
            return Response({'qualification' : False, 'list' : rere, 'num' : 5})

        # q6 : 반려 동물에 대한 가족 간 합의 여부
        if not survey['q6'] :
            return Response({'qualification' : False, 'list' : rere, 'num' : 6})

        # q7 : 우울증 여부
        if survey['q7'] : 
            return Response({'qualification' : False, 'list' : rere, 'num' : 7})

        # q8 : 이전 반려동물 중도포기 2회이상인가?
        if survey['q8'] :
            return Response({'qualification' : False, 'list' : rere, 'num' : 8})
        
        # q9 : 3인 이상의 가족, 실평수 10평이하 인가?
        if not survey['q9']:
            return Response({'qualification' : False, 'list' : rere, 'num' : 9})

        size = 0
        # q10 : 주거형태
        if survey['q10'] == 1:
            size = 1
        elif survey['q10'] == 2:
            size = 2
        elif survey['q10'] == 3:
            size = 3
        
        # q11 : 지출 가능 비용
        if survey['q11'] == 1:
            return Response({'qualification' : False, 'list' : rere, 'num' : 10})
        elif survey['q11'] == 2:
            size = 1
        elif survey['q11'] == 3:
            size = 2
        else:
            size = 3

        #size 1 : 소형견, 2 : 중형견이하, 3 : 대형견 이하        
        #사이즈, 털량, 활동량, 성격의 코사인 유사도가 높은 목록을 result에 저장
        '''
        result = self.recommend_dog(size, )

        #리스트에 있는 아이디를 가진 개의 정보를 json형식으로 rere에 추가한후, return
        for dog in result['dog_id']:
            rere.append(DogSerializer(self.get_object(dog)).data)
        '''
        return Response({'qualification' : True, 'size' : size, 'list' : rere, 'num' : 11})

