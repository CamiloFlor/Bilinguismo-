from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from usuarios.models import Detallesolicitud
from django.core import validators


from .models import TipoSolicitud
from django.contrib.auth.models import User



class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Detallesolicitud
        fields = '__all__'