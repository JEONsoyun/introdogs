from django.urls import path
from .views import DogList, DogFilter, FindDogByImg

urlpatterns = [
    path('/filter', DogList.as_view()),
    path('/<int:user_id>/', DogFilter.as_view()),
    path('/losts', FindDogByImg.as_view())
]
