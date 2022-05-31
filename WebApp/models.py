from datetime import date, datetime
from django.db import models

# Create your models here.
class Usuario(models.Model):
    email = models.CharField(max_length=100, unique=True, help_text="Dato unico")
    password = models.CharField(max_length=8)

class DatosUsuario(models.Model):
    idUsuario=models.IntegerField()
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    birthdate= models.DateField()
    telefono= models.CharField(max_length=100)
    genero= models.CharField(max_length=100)

class Musicos(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    instrumento= models.TextField()
    fecha_nacimiento= models.DateField()
    fecha_fallecimiento= models.DateField()
    acercade= models.TextField()

class Contacto(models.Model):    
    nombre= models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    descripcion= models.TextField()