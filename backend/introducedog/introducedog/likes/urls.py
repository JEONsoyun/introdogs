from django.urls import path
from .views import MakelikeView, DeletelikeView

urlpatterns = [
    path('', MakelikeView.as_view()),
    path('<str:dog_id>/', DeletelikeView.as_view()),
    # path('', LikelistView.as_view()),
]