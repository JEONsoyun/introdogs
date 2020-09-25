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
import sklearn
import pandas as pd

class DogMatch(APIView):
    def recommend_dog(self, colorin):
        dog_list = Dog.objects.all()
        serializer = DogSerializer(dog_list, many=True)
        data = serializer.data
        df = pd.DataFrame(data)

        df = df[['dog_id', 'kind', 'color']]
        
        counter_vector = CountVectorizer(ngram_range=(1, 3))
        c_vector_color = counter_vector.fit_transform(df['color'])
        color_c_sim = cosine_similarity(c_vector_color, c_vector_color).argsort()[:, ::-1]
        
        target_index = df[colorin == df['dog_id']].index.values
        #print(target_index)

        sim_index = color_c_sim[target_index, :30].reshape(-1)
        sim_index = sim_index[sim_index != target_index]
        #print(sim_index)

        result = df.iloc[sim_index]
        return result


    def get_object(self, dog_id):
        try:
            return Dog.objects.get(dog_id=dog_id)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        dog = self.get_object('N469569202000379')
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data
        color = data['color']

        dog_list = Dog.objects.all()
        serializer = DogSerializer(dog_list, many=True)
        
        result = self.recommend_dog('N447520202000218')
        for col in result['color']:
            print(col)

        rere = []
        for dog in result['dog_id']:
            rere.append(DogSerializer(self.get_object(dog)).data)
        
        return Response(rere)
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
'''
