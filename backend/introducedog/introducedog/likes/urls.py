from django.urls import path
<<<<<<< HEAD
from .views import MakelikeView, DeletelikeView

urlpatterns = [
    path('', MakelikeView.as_view()),
    path('/<str:dog_id>', DeletelikeView.as_view()),
    # path('', LikelistView.as_view()),
=======
from .views import MakelikeView, DeletelikeView, LikelistView

urlpatterns = [
    path('', MakelikeView.as_view()),
    path('<int:dog_id>', DeletelikeView.as_view()),
    path('',LikelistView.as_view()),
>>>>>>> develop_ssh_data
]