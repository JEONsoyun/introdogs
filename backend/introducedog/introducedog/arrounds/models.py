from django.db import models

# Create your models here.


class Shelter(models.Model):
    shelter_id = models.CharField(max_length=20, primary_key=True)  # 보호소번호
    shelter_name = models.CharField(max_length=128)  # 보호소 이름  careNm
    shelter_address = models.CharField(max_length=300)
    shelter_tel = models.CharField(max_length=20)
    charge_name = models.CharField(max_length=300)
    shelter_lat = models.CharField(max_length=128)
    shelter_lng = models.CharField(max_length=128)

    def __str__(self):
        return self.shelter_id
