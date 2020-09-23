from django.shortcuts import render

# Create your views here.
import json

from introducedog.settings import SECRET_KEY

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Dog


class DogList(View):
    def get(self, request):
        print("start")
        data = Dog.objects.values()
        return JsonResponse({"data": list(data)}, status=200)
