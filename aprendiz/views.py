from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from usuarios.models import Detallesolicitud, TipoSolicitud
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import TipoSolicitudForm, DetalleSolicitudForm
# Create your views here.
def inicio_aprendiz(request):
    return render(request, 'vistas/inicio_aprendiz.html',{
        'tituloventana': "Inicio"
    })

def crearsoli(request):
    user = User.objects.all()
    detallesolicitud= Detallesolicitud.objects.all()
    if request.method == 'POST':
        form_detallesolicitud = DetalleSolicitudForm(request.POST)
        if form_detallesolicitud.is_valid():
            form_detallesolicitud.save()
            return render(request,'vistas/soli.html')
    else:
        form_detallesolicitud = DetalleSolicitudForm()  # Crear una instancia del formulario correcto
    return render(request, 'vistas/soli.html', {'form_detallesolicitud': form_detallesolicitud, 'detallesolicitud': detallesolicitud, 'user': user})
def eliminar_tiposolicitud(request, id_detallesolicitud):
    detallesolicitud = Detallesolicitud.objects.get(id_detallesolicitud=id_detallesolicitud)
    detallesolicitud.delete()
    return redirect('inicio')