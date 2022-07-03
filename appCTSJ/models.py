from django.db import models

# Create your models here.
class Aplicacion_intermedia(models.Model):
    nombre=models.CharField(max_length=30)