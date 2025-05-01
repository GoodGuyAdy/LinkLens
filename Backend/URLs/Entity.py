from django.urls import path
from Backend.Views.Entity import EntityClass

urlpatterns = [
    path("entity", EntityClass.as_view()),
]