from django.shortcuts import render

# Create your views here.

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Dog


class DogList(View):
    def post(self, request):
        data = Dog.objects.values()
        return JsonResponse({"data": list(data)}, status=200)
