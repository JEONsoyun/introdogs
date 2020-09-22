import csv
import os
import django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "introducedog.settings")
django.setup()

from dogs.models import Dog

CSV_PATH = 'dog2.csv'

with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
	data_reader = csv.DictReader(csvfile)
	for row in data_reader:
		print(row)
		print(row[' end_date'])
		Dog.objects.create(
			dog_id=row['\ufeffdog_id'],
			shelter_name=row[' careNm'],
			age=re.findall("\d+",row[' age']),
			weight=re.findall("\d+",row[' weight']),
			sex=row[' sex'],
			kind=row[' kind'],
			color=row[' color'],
			neuter=row[' neuter'],
			thumnail=row[' thumnail'],
			careAddr=row[' careAddr'],
			special=row[' special'],
			find_place=row[' find_place '],
			find_date=row[' find_date '],
			end_date=row[' end_date'],
			
		)
