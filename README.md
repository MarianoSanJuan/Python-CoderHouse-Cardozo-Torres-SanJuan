Tutor Martín Bonnefoy Valdés
-Integrantes:
--Mariel Torres Ortiz
--Diego Cardozo
--Mariano San Juan

Se deben instalar los siguientes paquetes (ver archivo de requirements):
asgiref==3.5.2
Django==4.0.5
sqlparse==0.4.2
python3

Una vez descargado el repositorio de Github se deben seguir los siguientes pasos:
Iniciar entorno virtual con: 
. venv/bin/activate (para Mac) o . venv/Script/activate (para Windows)
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver