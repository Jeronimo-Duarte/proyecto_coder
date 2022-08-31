from django.contrib import admin
from django.urls import path
from app_coder import views 

urlpatterns = [
    path('',views.inicio),
    path('estudiantes',views.estudiantes),
    path('entregables',views.entregables),
    path('profesores',views.profesores),
    path('curso',views.curso),
]