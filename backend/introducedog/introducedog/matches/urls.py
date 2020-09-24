from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from matches.views import DogMatch

urlpatterns = [
    path('dogs/', DogMatch.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)