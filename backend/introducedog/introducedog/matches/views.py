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


class DogColorMatch(APIView):
    def recommend_dog(self, colorin):
        dog_list = Dog.objects.all()
        serializer = DogSerializer(dog_list, many=True)
        data = serializer.data
        df = pd.DataFrame(data)

        df = df[['dog_id', 'kind', 'color']]
        # df에 사용자가 입력한 색을 가지는 가상의 개를 만들어서 넣어 코사인 유사도를 구한다.
        df = df.append({'dog_id': 'N011', 'kind': '투명',
                        'color': str(colorin)}, ignore_index=True)
        # CountVectorizer
        counter_vector = HashingVectorizer(ngram_range=(1, 3))
        c_vector_color = counter_vector.fit_transform(df['color'])
        color_c_sim = cosine_similarity(
            c_vector_color, c_vector_color).argsort()[:, ::-1]

        target_index = df['N011' == df['dog_id']].index.values
        print(target_index)

        sim_index = color_c_sim[target_index, :30].reshape(-1)
        sim_index = sim_index[sim_index != target_index]
        print(sim_index)

        result = df.iloc[sim_index]
        return result

    # dog_id에 해당하는 dog를 return해준다, 없다면 http404
    def get_object(self, dog_id):
        try:
            return Dog.objects.get(dog_id=dog_id)
        except Dog.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        # reqeust에서 넘어온 값에서 color값을 뽑음
        data = request.data
        color = data['color']

        # 해당 컬러와 유사도가 높은 개 목록을 result에 저장
        result = self.recommend_dog(color)
        for col in result['color']:
            print(col)

        # 리스트에 있는 아이디를 가진 개의 정보를 json형식으로 rere에 추가한후, return
        rere = []
        for dog in result['dog_id']:
            rere.append(DogSerializer(self.get_object(dog)).data)

        return Response(rere)
