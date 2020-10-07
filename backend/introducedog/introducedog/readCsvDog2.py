from dogs.models import Dog
import csv
import os
import django
import re
# 실행방법 : 현재 위치로 이동 한다 .
# python manage.py shell을 친다
# 복붙 한다ㅋㅋㅋㅋㅋㅋ
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "introducedog.settings")
django.setup()


CSV_PATH = 'dog_tel_20201007.csv'

with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        print(row['end_date'])
        print(type(row['end_date']))
        dog_id = row['\ufeffdog_id']
        print(dog_id)
        shelter_name = row['careNum']
        print(shelter_name)
        age = re.findall("\d+", row['age'])
        print(age)
        weight = row['weight'][:-4]
        print(weight)
        sex = row['sex']
        print(sex)
        kind = row['kind']
        print(kind)
        color = row['color']
        print(color)
        neuter = row['neuter']
        print(neuter)
        thumnail = row['thumnail']
        print(thumnail)
        careAddr = row['careAddr']
        print(careAddr)
        special = row['special']
        print(special)
        find_place = row['find_place']
        print(find_place)
        find_date = row['find_date']
        print(find_date)
        end_date = row['end_date']
        print(end_date)
        d = Dog(
            dog_id=row['\ufeffdog_id'],
            shelter_name=row['careNum'],
            age=re.findall("\d+", row['age'])[0],
            weight=re.findall("\d+", row['weight'])[0],
            sex=row['sex'],
            kind=row['kind'],
            color=row['color'],
            neuter=row['neuter'],
            thumnail=row['thumnail'],
            profile=row['profile'],
            careAddr=row['careAddr'],
            special=row['special'],
            find_place=row['find_place'],
            find_date=row['find_date'],
            end_date=row['end_date']
        )
        print(d)
        d.save()
