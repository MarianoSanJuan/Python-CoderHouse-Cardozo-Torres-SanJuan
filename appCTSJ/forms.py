from django import forms 


class formPersonas(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    
class busquedaPersona(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)