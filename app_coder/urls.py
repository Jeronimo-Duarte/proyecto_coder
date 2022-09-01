from django.contrib import admin
from django.urls import path
from app_coder import views 

urlpatterns = [
    path('',views.inicio),
    path('estudiantes',views.estudiantes,name="estudiantes"),
    path('entregables',views.entregables,name="entregables"),
    path('profesores',views.profesores,name="profesores"),
    path('curso',views.curso,name="curso"),
]