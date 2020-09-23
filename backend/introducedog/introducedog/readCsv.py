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
		print(type(row[' end_date']))
		dog_id=row['\ufeffdog_id']
		print(dog_id)
		shelter_name=row[' careNm']
		print(shelter_name)
		age=re.findall("\d+",row[' age'])
		print(age)
		weight=re.findall("\d+",row[' weight'])
		print(weight)
		sex=row[' sex']
		print(sex)
		kind=row[' kind']
		print(kind)
		color=row[' color']
		print(color)
		neuter=row[' neuter']
		print(neuter)
		thumnail=row[' thumnail']
		print(thumnail)
		careAddr=row[' careAddr']
		print(careAddr)
		special=row[' special']
		print(special)
		find_place=row[' find_place ']
		print(find_place)
		find_date=row[' find_date ']
		print(find_date)
		end_date=row[' end_date']
		print(end_date)
		d = Dog(
			dog_id=row['\ufeffdog_id'],
			shelter_name=row[' careNm'],
			age=re.findall("\d+",row[' age'])[0],
			weight=re.findall("\d+",row[' weight'])[0],
			sex=row[' sex'],
			kind=row[' kind'],
			color=row[' color'],
			neuter=row[' neuter'],
			thumnail=row[' thumnail'],
			careAddr=row[' careAddr'],
			special=row[' special'],
			find_place=row[' find_place '],
			find_date=row[' find_date '],
			end_date=row[' end_date']
		)
		print(d)
		d.save()