from django.shortcuts import render

# Create your views here.

import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from dogs.models import Dog
from arrounds.models import Shelter

class DetaildogView(View):
    def get(self, request, dog_id):
        # print(dog_id)
        doglist = Dog.objects.filter(dog_id = dog_id).values()
        shelter_name = ""
        for one_dog in doglist:
            shelter_name = one_dog['shelter_name']
            one_dog['shelter'] = []
            shelter_info = Shelter.objects.filter(shelter_name = shelter_name).values()
            for one_shelter in shelter_info:
                one_dog['shelter'].append(one_shelter)
        
            
        # print(doglist)
        return JsonResponse({'dog_info':list(doglist)}, status=200)