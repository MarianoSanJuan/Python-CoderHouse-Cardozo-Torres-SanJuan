from django.shortcuts import render,HttpResponse
from django.template import loader

# Create your views here.

# Definición de view de la home

# def view_home(request):
#     template = loader.get_template("home.html")
#     render = template.render({})
#     return HttpResponse(render)

# Otra alternativa para la view de la home

def view_home(request):
    return render(request,"home.html",{})
 