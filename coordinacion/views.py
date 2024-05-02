# Importación de las funciones y clases necesarias desde los módulos de Django
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from usuarios.models import Detallesolicitud
from django.urls import reverse

# Definición de las vistas

# Vista para la página de inicio de coordinación
def inicio_coordinacion(request):
    # Renderiza la plantilla 'inicio_coordinacion.html' con el título de la ventana
    return render(request, 'vistas/inicio_coordinacion.html', {
        'tituloventana': "Inicio"
    })

# Vista para la página de noticias
def noticias(request):
    # Renderiza la plantilla 'noticias.html'
    return render(request, 'vistas/noticias.html')

# Vista para la página de actualización de perfil
def actualizarperfil(request):
    # Renderiza la plantilla 'actualizarperfil.html'
    return render(request, 'vistas/actualizarperfil.html')

# Vista para la página de gestión de permisos
def gestiondepermisos(request):
    # Renderiza la plantilla 'gestiondepermisos.html'
    return render(request, 'vistas/gestiondepermisos.html')


