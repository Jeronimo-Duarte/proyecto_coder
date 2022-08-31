from django.db import models

# Create your models here.

class Estudiantes(models.Model):
    nombre = models.CharField(null=False,max_length=128)
    apellido = models.CharField(null=False,max_length=128)
    email = models.EmailField()
    


class Profesor(models.Model):
    nombre = models.CharField(null=False,max_length=128)
    apellido = models.CharField(null=False,max_length=128)
    email = models.EmailField()
    profesion= models.CharField(null=False,max_length=64)
    


class Curso(models.Model):
    nombre = models.CharField(null=False,max_length=128)
    comision = models.IntegerField()
   


class Entregable(models.Model):
    nombre = models.CharField(null=False,max_length=128)
    entregado= models.BooleanField()
    fecha_de_entrega= models.DateField()