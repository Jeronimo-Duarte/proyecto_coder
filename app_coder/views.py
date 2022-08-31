from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from app_coder.models import Estudiantes
# Create your views here.

def estudiantes(request):
    estudiantes= Estudiantes.objects.all()
    diccionario={'estudiantes':estudiantes}
    plantilla= loader.get_template("plantilla1.html")
    documento_html= plantilla.render(diccionario)
    return HttpResponse(documento_html)


