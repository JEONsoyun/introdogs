from rest_framework import serializers
from dogs.models import Dog

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id','dog_id','shelter_name','age','weight','sex','kind','color','neuter','thumnail','profile','careAddr','special','find_place','find_date','end_date']

