
import csv
import os
import django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "introducedog.settings")
django.setup()
from arrounds.models import Shelter
CSV_PATH = 'shelterU.csv'

with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        print(row['shelter_id'])
        print(type(row['shelter_id']))
        shelter_name = row['\ufeffshelter_name']
        print(shelter_name)
        shelter_id = row['shelter_id']
        print(shelter_id)
        shelter_address = row['shelter_address']
        print(shelter_address)
        shelter_lat = row['shelter_lat']
        print(shelter_lat)
        shelter_lng = row['shelter_lng']
        print(shelter_lng)
        shelter_tel = row['shelter_tel']
        print(shelter_tel)
        s = Shelter(
            shelter_name=shelter_name,
            shelter_id=shelter_id,
            shelter_address=shelter_address,
            shelter_lat=shelter_lat,
            shelter_lng=shelter_lng,
            shelter_tel=shelter_tel
        )
        print(s)
        s.save()
