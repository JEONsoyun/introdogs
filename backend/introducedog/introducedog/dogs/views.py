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
