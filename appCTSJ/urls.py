from django.urls import  path
from .views import view_home, herencia

urlpatterns = [
    path('', view_home),
    path('about/', herencia),
]