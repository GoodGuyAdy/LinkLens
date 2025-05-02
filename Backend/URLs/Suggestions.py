from django.urls import path
from Backend.Views.Suggestions import SuggestionsClass

urlpatterns = [
    path("suggestions", SuggestionsClass.as_view()),
]
