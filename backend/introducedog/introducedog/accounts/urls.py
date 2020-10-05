from django.urls import path
from .views import SignupView, LoginView, LogoutView, MypageView, ApicheckView

from rest_framework.routers import DefaultRouter
from .views import FileTestViewSet

router = DefaultRouter()
router.register(f'file', FileTestViewSet)


urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('mypage/', MypageView.as_view()),
    path('islogin/', ApicheckView.as_view()),
]
