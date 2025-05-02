from django.urls import path
from Backend.Views.Chat import DatabaseChatClass

urlpatterns = [
    path("chat", DatabaseChatClass.as_view()),
]
