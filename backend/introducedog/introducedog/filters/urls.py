from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from filters.views import DogColorMatch, DogColorContainMatch

urlpatterns = [
    #path('pre/', DogColorMatch.as_view()),
    path('', DogColorContainMatch.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)