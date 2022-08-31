from django.contrib import admin
from django.urls import path
from app_coder.views import estudiantes



urlpatterns = [
    path('',estudiantes),
]