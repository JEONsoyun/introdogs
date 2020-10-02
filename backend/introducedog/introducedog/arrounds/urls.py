from django.urls import path
from .views import Aroundshelter, FindShelterDog

urlpatterns = [
    path('/shelters', Aroundshelter.as_view()),
    path('/shelter', FindShelterDog.as_view()),
    path('/<str:shelter_name>', FindShelterDog.as_view()),

]
