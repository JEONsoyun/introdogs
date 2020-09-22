from django.db import models

# Create your models here.


class Dog(models.Model):
    dog_id = models.CharField(max_length=20, null=True)  # 유기번호
    shelter_name = models.CharField(max_length=128)  # 보호소 이름  careNm
    age = models.IntegerField()
    weight = models.IntegerField()  # 유기동물 몸무게(weight)
    sex = models.CharField(max_length=10, default='Q')  # 유기동물 성별(sex)
    kind = models.CharField(max_length=128)  # 유기동물 종 ()
    color = models.CharField(max_length=128)  # 유기동물 색깔
    neuter = models.CharField(max_length=10)
    thumnail = models.CharField(max_length=300)
    profile = models.CharField(max_length=300)
    careAddr = models.CharField(max_length=300)
    special = models.CharField(max_length=300)
    find_place = models.CharField(max_length=300)
    find_date = models.IntegerField()
    end_date = models.IntegerField()

    def __str__(self):
        return self.dog_id
