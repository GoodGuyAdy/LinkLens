from django.urls import path
from Backend.Views.User import UserClass

urlpatterns = [
    path("user", UserClass.as_view()),
]