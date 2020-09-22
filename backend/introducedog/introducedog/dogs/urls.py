from django.urls import path
from .views import SignupView, LoginView, LogoutView, MypageView, ApicheckView

urlpatterns = [
    path('/filter', SignupView.as_view()),
]
