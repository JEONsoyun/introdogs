from django.urls import path
from .views import MakelikeView, DeletelikeView, LikelistView

urlpatterns = [
    path('', MakelikeView.as_view()),
    path('<int:dog_id>', DeletelikeView.as_view()),
    path('',LikelistView.as_view()),
]