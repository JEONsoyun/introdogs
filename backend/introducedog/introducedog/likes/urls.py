from django.urls import path
from .views import MakelikeView, DeletelikeView

urlpatterns = [
    path('', MakelikeView.as_view()),
    path('<str:dog_id>/', DeletelikeView.as_view()),
    # path('', LikelistView.as_view()),
<<<<<<< HEAD
<<<<<<< HEAD
]
=======
]
>>>>>>> origin/develop-cj
=======
]
>>>>>>> origin/develop_ssh_data
