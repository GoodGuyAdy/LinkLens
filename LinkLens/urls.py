"""
URL configuration for LinkLens project.
"""

from django.contrib import admin
from django.urls import path, include
from Constants.URL_Constants import PROJECT_URL_PREFIX

urlpatterns = [
    path("admin/", admin.site.urls),
    path(PROJECT_URL_PREFIX, include("Backend.URLs.User")),
    path(PROJECT_URL_PREFIX, include("Backend.URLs.Entity")),
    path(PROJECT_URL_PREFIX, include("Backend.URLs.Event")),
    path(PROJECT_URL_PREFIX, include("Backend.URLs.Suggestions")),
    path(PROJECT_URL_PREFIX, include("Backend.URLs.Chat")),
]
