from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
# Create your views here.

def inicio(request):
    return render(request, "app_coder/inicio.html")


def profesores(request):
    return render(request, "app_coder/profesores.html")


def curso(request):
    
    return render(request, "app_coder/curso.html")

def entregables(request):
    return render(request, "app_coder/entregables.html")


def estudiantes(request):
    return render(request, "app_coder/estudiantes.html")