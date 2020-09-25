from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    path = serializers.FileField(required=False)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', )