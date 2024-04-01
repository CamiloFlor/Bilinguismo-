from django.shortcuts import render,redirect


# Create your views here.

def inicio(request):
    return render(request, 'vistas/inicio.html',{
        'tituloventana': "Inicio"
    })
def crearsoli(request):
    # usuario = Usuarios.objects.all()
    return render(request, 'vistas/soli.html',{
        'tituloventana': "Solicitud"
    })

def noticias(request):
    return render(request, 'vistas/noticias.html',{
        'tituloventana': "noticias"
    })