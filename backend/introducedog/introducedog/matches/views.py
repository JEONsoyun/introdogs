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
    def find_breed_list(self, pick):
        '''
        1. 말티즈/ 진도견/ 포메
        2. 푸들 / 치와와 /닥스훈트
        3. 요크셔테리어/리트리버/ 시츄
        '''
        #print(pick)

        #고른 종의 성격을 합하여 선호하는 성격의 가상견을 생성한다.

        doglist = [['젠틀 장난 매력','경고 지능 대담', '호기심 대담 생동감'], 
                    ['다정 친절 독립 민첩 지능 자신감', '챠밍 우아함 콧대', '친절 호기심 섹시'], 
                    ['다정 멋짐 말괄량이','친절 지능 헌신', '다정 장난 외향']]

        sum =''
        for i in range(3):
            key = 'p'+ str(i+1)
            sum += ' ' + doglist[i][pick[key]-1]
        
        #print(sum)

        #가상의 개를 추가하여 consin 유사도를 이용해 비슷한 성격의 종 목록을 얻는다.
        #size 1 : 소형견, 2 : 중형견이하, 3 : 대형견 이하
        df = pd.DataFrame({'name' : ['말티즈', '진도견', '푸들', '포메라니안', '치와와', '시츄', '닥스훈트', '골든 리트리버', '요크셔 테리어'],
                            'character' : ['젠틀 장난 매력','경고 지능 대담','다정 친절 독립 민첩 지능 자신감','호기심 대담 생동감','챠밍 우아함 콧대',
                            '다정 장난 외향','친절 호기심 섹시', '친절 지능 헌신', '다정 멋짐 말괄량이']})

        df = df.append({'name' : '가상', 'character' : sum}, ignore_index=True)
        #print(df)

        #CountVectorizer
        counter_vector = HashingVectorizer(ngram_range=(1, 3))
        c_vector_character = counter_vector.fit_transform(df['character'])
        character_c_sim = cosine_similarity(c_vector_character, c_vector_character).argsort()[:, ::-1]
        
        target_index = df['가상' == df['name']].index.values
        #print(target_index)

        sim_index = character_c_sim[target_index].reshape(-1)
        sim_index = sim_index[sim_index != target_index]
        #print(sim_index)

        result = df.iloc[sim_index]
        return result['name']


    def recommend_dog(self, size, breeds):
        dog_list = Dog.objects.all()
        serializer = DogSerializer(dog_list, many=True)
        data = serializer.data
        df = pd.DataFrame(data)

        #현재 데이터에 존재하는 강아지 사이즈(102)
        dogsize = {'골든 리트리버':3, '그레이 하운드':3, '그레이트 덴':3, '그레이트 피레니즈':3, '그레이하운드' :3, '기타': 2, '닥스훈트': 1, '달마시안': 3, '도베르만':3, '도사':3,
            '동경견': 2, '딩고': 3, '라브라도 리트리버': 3, '레이크랜드 테리어': 3, '롯트와일러' :2, '리트리버': 3, '말라뮤트' :3, '베들링턴 테리어':2, '베를링턴 테리어':2, '벨지안 셰퍼드 독':3,'보더 콜리':3,'보더콜리':3,'보스턴 테리어':1, '불 테리어':1, '불독':1,
            '말티즈':1, '말티푸': 1, '미니어쳐 푸들': 1, '미니어쳐 핀셔': 1, '미텔 스피츠': 2, '믹스': 2, '믹스견': 2, '바셋 하운드': 1, '발바리': 1, '발발이': 1,
            '진도견':3, '푸들' : 2, '포메라니안' : 1, '치와와' : 1, '시츄' : 1, '요크셔 테리어':1}

        result = []

        #print(breeds)

        for breed in breeds:
            if dogsize[breed] > size:
                continue
            else :
                #print(breed)
                #해당 종을 result에 넣어주기
                for dog in data:
                    if dog['kind'] == breed:
                        result.append(dog['dog_id'])            
        
        return result

    #dog_id에 해당하는 dog를 return해준다, 없다면 http404
    def get_object(self, dog_id):
        try:
            return Dog.objects.get(dog_id=dog_id)
        except Dog.DoesNotExist:
            raise Http404
    
    def post(self, request, format=None):
         #reqeust에서 넘어온 값에서 data을 뽑음
        data = request.data
        '''
        {"pick" : {
            "p1" : 1,
            "p2" : 1,
            "p3" : 3
            }, 
            "survey" : {
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
        #사진 속 개 종의 성격을 합쳐 그에 비슷한 성격의 종들의 목록(breeds)를 준다.
        pick = data['pick']
        breeds = self.find_breed_list(pick)
        #print(breeds)

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
        #사이즈, 성격의 코사인 유사도가 높은 목록을 result에 저장
        result = self.recommend_dog(size, breeds)
        #print(result)
        result = result[30:]

        #리스트에 있는 아이디를 가진 개의 정보를 json형식으로 rere에 추가한후, return
        for dog in result:
            rere.append(DogSerializer(self.get_object(dog)).data)
        
        return Response({'qualification' : True, 'size' : size, 'list' : rere, 'num' : 11})

