from django.shortcuts import render

# Create your views here.
import json

from introducedog.settings import SECRET_KEY

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Dog


class DogList(View):
    def get(self, request):
        print("full Dog List")
        data = Dog.objects.values()
        return JsonResponse({"data": list(data)}, status=200)


class DogFilter(View):
    def get(self, request, user_id):
        print(user_id)
        return True
