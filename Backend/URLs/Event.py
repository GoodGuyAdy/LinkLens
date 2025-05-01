from django.urls import path
from Backend.Views.Event import EventClass

urlpatterns = [
    path("event", EventClass.as_view()),
]
