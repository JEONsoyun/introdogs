from django.urls import path
from .views import DogList

urlpatterns = [
    path('/filter', DogList.as_view()),
]
