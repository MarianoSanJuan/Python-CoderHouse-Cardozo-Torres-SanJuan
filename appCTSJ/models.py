from django.db import models
from django.forms import ModelForm

# Create your models here.
class Aplicacion_intermedia(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    
    def __str__(self):
        return f'nombre: {self.nombre}'
    