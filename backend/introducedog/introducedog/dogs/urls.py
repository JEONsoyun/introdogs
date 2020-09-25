from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from dogs import views
from .views import DogList, DogFilter, FindDogByImg

urlpatterns = [
    path('/filter', DogList.as_view()),
    path('/<int:user_id>/', DogFilter.as_view()),
    path('<int:user_id>/', DogFilter.as_view()),
    path('losts/', FindDogByImg.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)