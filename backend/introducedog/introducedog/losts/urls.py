from django.urls import path
from .views import FindDogByImg

urlpatterns = [
    path('', FindDogByImg, name='findDogByImg'),
    #path('/<str:dog_id>', DeletelikeView.as_view()),
    # path('', LikelistView.as_view()),
]
