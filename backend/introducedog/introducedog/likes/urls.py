from django.urls import path
from .views import MakelikeView, DeletelikeView
# from .views import SignupView, LoginView, LogoutView, MypageView, ApicheckView

urlpatterns = [
    path('', MakelikeView.as_view()),
    path('/<int:dog_id>', DeletelikeView.as_view()),
    # path('/signup', SignupView.as_view()),
    # path('/login', LoginView.as_view()),
    # path('/logout', LogoutView.as_view()),
    # path('/mypage', MypageView.as_view()),
    # path('/islogin', ApicheckView.as_view()),
]