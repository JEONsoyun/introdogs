from django.shortcuts import render

# Create your views here.

import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from dogs.models import Dog

class DetaildogView(View):
    def get(self, request, dog_id):
        # print(dog_id)
        doglist = Dog.objects.filter(dog_id = dog_id).values()
        # print(doglist)
        return JsonResponse({'dog_info':list(doglist)}, status=200)