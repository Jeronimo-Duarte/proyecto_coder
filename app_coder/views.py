from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context,loader
from app_coder.models import *
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
    estudiantes= Estudiantes.objects.all()
    diccionario= {"estudiantes":estudiantes}
    plantilla= loader.get_template("app_coder/estudiantes.html")
    documento_html= plantilla.render(diccionario)
    return HttpResponse(documento_html)