from django.urls import path
# from .views import DogList, DogFilter
from .views import Aroundshelter

urlpatterns = [
    # path('/filter', DogList.as_view()),
    # path('/<int:user_id>/', DogFilter.as_view()),
    path('/shelter', Aroundshelter.as_view()),
]
