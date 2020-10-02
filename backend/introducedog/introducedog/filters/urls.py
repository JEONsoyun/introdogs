from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from filters.views import DogColorMatch

urlpatterns = [
    path('', DogColorMatch.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)