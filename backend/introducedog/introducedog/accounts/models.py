from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True) #사용자 id
    user_name = models.CharField(max_length=128, null=True) #사용자 이름
    user_email = models.CharField(max_length=128, null=True) #사용자 email
    user_password = models.CharField(max_length=128, null=True) #사용자 password
    user_profile = models.FileField(blank=True, null=True) #사용자 프로필 사진
    match_dog = models.CharField(max_length=300, null=True) #사용자와 잘 어울리는 강아지 id
    same_dog = models.CharField(max_length=300, null=True) #사용자와 닮은 강아지 id
    