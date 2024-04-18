from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio_coordinacion(request):
    return render(request, 'vistas/inicio_coordinacion.html',{
        'tituloventana': "Inicio"
    })
def noticias(request):
    return render(request, 'vistas/noticias.html',{
        'tituloventana': "noticias"
    })