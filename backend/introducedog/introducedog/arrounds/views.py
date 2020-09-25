from django.shortcuts import render

# Create your views here.
import json
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Shelter
from likes.models import Like
from dogs.models import Dog
from accounts.models import User


from haversine import haversine


class Aroundshelter(View):
    def post(self, request):
        data = json.loads(request.body)
        myuser = User.objects.filter(user_name = request.session.get('username')).values()
        userid = myuser[0]['user_id']
        user = {}
        my_lat  = float(data['shelter_lat'])
        my_lng = float(data['shelter_lng'])
        st = (my_lat, my_lng)
        shelters = Shelter.objects.values()
        ret = []
        for shel in shelters:
            shel_lat = shel['shelter_lat']
            shel_lng = shel['shelter_lng']
            end = (float(shel_lat), float(shel_lng))
            if haversine(st, end) <11 :
                ret.append(shel)
        
        return JsonResponse(ret, safe=False)
