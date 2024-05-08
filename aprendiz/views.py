from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from usuarios.models import Detallesolicitud, TipoSolicitud
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import TipoSolicitudForm, DetalleSolicitudForm

                                                                                                                # Define your views here
def inicio_aprendiz(request):
                                                                                                                # Render the 'inicio_aprendiz.html' template with the window title "Inicio"
    return render(request, 'vistas/inicio_aprendiz.html', {
        'tituloventana': "Inicio"
    })

def crearsoli(request):
                                                                                                                # Se obtienen todos los usuarios y todos los detalles de solicitud
    user = User.objects.all()
    detallesolicitud= Detallesolicitud.objects.all()
    
    if request.method == 'POST':
                                                                                                                # Si la solicitud es de tipo POST, se procesa el formulario
        form_detallesolicitud = DetalleSolicitudForm(request.POST)
        if form_detallesolicitud.is_valid():
                                                                                                                # Si el formulario es válido, se guarda
            form_detallesolicitud.save()
                                                                                                                # Se renderiza la página 'soli.html'
            return render(request,'vistas/soli.html')
    else:
                                                                                                                # Si la solicitud no es de tipo POST, se crea una instancia del formulario
        form_detallesolicitud = DetalleSolicitudForm()
    
                                                                                                                # Se renderiza la página 'soli.html' con el formulario y los detalles de solicitud
    return render(request, 'vistas/soli.html', {'form_detallesolicitud': form_detallesolicitud, 'detallesolicitud': detallesolicitud, 'user': user})



def eliminar_tiposolicitud(request, id_detallesolicitud):
                                                                                                                # Se obtiene el objeto Detallesolicitud correspondiente al ID proporcionado
    detallesolicitud = Detallesolicitud.objects.get(id_detallesolicitud=id_detallesolicitud)
                                                                                                                # Se elimina el objeto Detallesolicitud de la base de datos
    detallesolicitud.delete()
                                                                                                                # Se redirige al usuario a la vista 'inicio'
    return redirect('inicio')
