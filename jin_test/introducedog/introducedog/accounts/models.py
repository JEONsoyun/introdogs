from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    # id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=128, null=True)
    user_email = models.CharField(max_length=128, null=True)
    user_password = models.CharField(max_length=128, null=True)
    user_profile = models.CharField(max_length=300, null=True)
    match_dog = models.IntegerField( null=True)
    same_dog = models.CharField(max_length=300, null=True)
    