from django import forms 


class FormPersonas(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    
class BusquedaPersona(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)