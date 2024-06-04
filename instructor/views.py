
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio_instructor(request):
    return render(request, 'vistas/inicio_instructor.html',{
        'tituloventana': "Inicio"
    })

def noti_instru(request):
    noticia = Noticia.objects.all()
    return render(request, 'noti/index.html', {'noti': noticia})

def crear_instru(request):
    formulario = NoticiaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('noti')
    return render(request, 'noti/crear.html', {'formulario': formulario})
def editar_instru(request, id):
    noti = Noticia.objects.get(id=id)
    formulario = NoticiaForm(request.POST or None, request.FILES or None, instance=noti) 
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('noti_instru') 
    return render(request, 'noti/editar.html',{'formulario':formulario } )


def eliminar_instru(request, id ):
    noti = Noticia.objects.get(id=id)
    noti.delete()
    return redirect('noti_instru')


def noticias(request):
    return render(request, 'vistas/noticias.html',{
        'tituloventana': "noticias"
    })
    

def crearsoli_instructor(request):
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
def eliminartiposoli_instructor(request, id_detallesolicitud):
    detallesolicitud = Detallesolicitud.objects.get(id_detallesolicitud=id_detallesolicitud)
    detallesolicitud.delete()
    return redirect('inicio')