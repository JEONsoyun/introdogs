from django.urls import path
from .views import DetaildogView

urlpatterns = [
    path('<str:dog_id>/', DetaildogView.as_view()),
    
]