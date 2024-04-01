from django.core import validators
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        # crea automaticamente los campos que queremos
        model = Usuarios
        # la lista de lo que queremos
        fields =['numeroiden', 'nombre', 'correo']


class subirnoticia(UserCreationForm):
    class  Meta:
        model = tiposolicitud

        fields = ['nombre','descripcion','archivo','url','fecha_fin','fecha_inicio', ]