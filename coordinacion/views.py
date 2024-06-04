
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
def noticias(request):                                                                   # Vista para la página de noticias
      return render(request, 'vistas/noticias.html')                                     # Renderiza la plantilla 'noticias.html'

def actualizarperfil(request):                                                          # Vista para la página de actualización de perfil
       return render(request, 'vistas/actualizarperfil.html')                           # Renderiza la plantilla 'actualizarperfil.html'

def gestiondepermisos(request):                                                         # Vista para la página de gestión de permisos
       return render(request, 'vistas/gestiondepermisos.html')



