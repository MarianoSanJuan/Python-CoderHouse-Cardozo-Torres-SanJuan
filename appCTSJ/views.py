from re import template
from django.shortcuts import render,HttpResponse
from django.template import loader
from appCTSJ.forms import BusquedaPersona, FormPersonas
from appCTSJ.models import Modelo_personas

# Create your views here.

# Definición de view de la homels

def view_home(request):
    
    return render(request,"home.html",{})
    
  
def herencia(request):
    return render(request,"template_herencia.html",{})


def formulario(request):
    

    if request.method == 'POST':
        form = FormPersonas(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            
            personas = Modelo_personas(
                nombre = data.get('nombre'),
                apellido = data.get('apellido'),
                edad = data.get('edad'))
            personas.save()

            listado_persona = Modelo_personas.objects.all()
                   
            return render(request,'listado_personas.html',{"listado_persona":listado_persona})
        
        else:
            return render(request,'formulario.html',{'form':form})
            
    else:
        form = FormPersonas()
        return render(request,'formulario.html',{'form':form})
    


def listado_persona(request):
    
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        listado_persona = Modelo_personas.objects.filter(nombre__icontains=nombre_de_busqueda)
    else:    
        listado_persona = Modelo_personas.objects.all()
    form = BusquedaPersona()
    return render(request,'listado_personas.html',{'listado_persona': listado_persona, "form": form})

