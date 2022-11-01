from xml.dom.minidom import Identified
from django.db import models

# Create your models here.

class Actividad(models.Model):
      id = models.BigAutoField(primary_key=True)
      descripcion = models.CharField("Descripción", max_length=100)
      responsable = models.CharField("Responsable", max_length=50)
      
class Estado(models.Model):
      id = models.BigAutoField(primary_key=True)
      nombre= models.CharField("Nombre: ",max_length=255)