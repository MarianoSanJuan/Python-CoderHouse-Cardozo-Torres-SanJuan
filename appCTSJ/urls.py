from django.urls import  path
from .views import view_home, herencia, formulario
# from .views import view_home, herencia, formulario, listado_persona

urlpatterns = [
    path('', view_home, name='home'),
    path('about/', herencia, name='about'),
    path('formulario/',formulario, name='formulario'),
    # path('listado-persona/',listado_persona, name='listado_persona'),
    
]