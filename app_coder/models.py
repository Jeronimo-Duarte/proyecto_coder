from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(null=False,max_length=128)
    apellido = models.CharField(null=False,max_length=128)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    


class Profesor(models.Model):
    nombre = models.CharField(null=False,max_length=128)
    apellido = models.CharField(null=False,max_length=128)
    email = models.EmailField()
    profesion= models.CharField(null=False,max_length=64)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Curso(models.Model):
    nombre = models.CharField(null=False,max_length=128)
    comision = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} {self.comision}'
   


class Entregable(models.Model):
    nombre = models.CharField(null=False,max_length=128)
    entregado= models.BooleanField()
    fecha_de_entrega= models.DateField()

    def __str__(self):
        return f'{self.nombre}'