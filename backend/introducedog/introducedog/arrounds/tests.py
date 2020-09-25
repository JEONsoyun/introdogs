from django.test import TestCase

# Create your tests here.
from geopy import distance

from haversine import haversine

def get_distance():
    st = (float(37.8701158122), float(126.9835430508))
    end = (float(37.8459716369), float(127.4986540628))
    print("sksk")
    print(haversine(st, end))