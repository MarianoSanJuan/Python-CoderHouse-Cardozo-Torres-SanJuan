from re import template
from django.shortcuts import render,HttpResponse
from django.template import loader
from appCTSJ.models import Aplicacion_intermedia

# Create your views here.

# Definición de view de la homels

# def view_home(request):
#     template = loader.get_template("home.html")
#     render = template.render({})
#     return HttpResponse(render)

# Otra alternativa para la view de la home

def view_home(request):
    return render(request,"home.html",{})
 
def herencia(request):
    return render(request,"template_herencia.html",{})
 

    

