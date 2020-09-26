from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from dogs import views
from .views import DogList, DogFilter, FindDogByImg

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/develop_ssh_data
    path('dogs/', views.DogList.as_view()),
    path('details/<str:dog_id>/', views.DogDetail.as_view()),
    #path('/filter', DogList.as_view()),
    path('<int:user_id>/', DogFilter.as_view()),
    path('losts/', FindDogByImg.as_view())
<<<<<<< HEAD
=======
    path('/filter', DogList.as_view()),
    path('/<int:user_id>/', DogFilter.as_view()),
    path('<int:user_id>/', DogFilter.as_view()),
    path('losts/', FindDogByImg.as_view()),
    
>>>>>>> origin/develop-cj
=======
>>>>>>> origin/develop_ssh_data
]

urlpatterns = format_suffix_patterns(urlpatterns)
