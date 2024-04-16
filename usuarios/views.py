from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from usuarios.forms import RegisterForm, UserProfileForm, DetalleSolicitudForm, TipoDocumentoForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from usuarios.models import Rol, UserProfile, Detallesolicitud, Tipodocumento
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

def inicio_usuarios(request):
    return render(request, 'vistas/inicio.html',{
        'tituloventana': "Inicio"
    })
def registro(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if register_form.is_valid() and userprofile_form.is_valid():
            user = register_form.save()
            user_profile = userprofile_form.save(commit=False)
            user_profile.user = user
            user_profile.id_rol = userprofile_form.cleaned_data['id_rol']  # Asigna el id_rol seleccionado en el formulario
            user_profile.save()
            return redirect('inicio_usuarios')
    else:
        register_form = RegisterForm()
        userprofile_form = UserProfileForm()
    roles = Rol.objects.all()
    return render(request, 'users/registro.html', {
        'title': 'Registro',
        'roles': roles,
        'register_form': register_form,
        'userprofile_form': userprofile_form,  # Asegúrate de pasar el formulario de UserProfile a la plantilla
    })
def login_user(request):
    if request.user.is_authenticated:
        return redirect('inicio_usuarios')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    user_profile = UserProfile.objects.get(user=user)
                    rol = user_profile.id_rol
                    if rol.id_rol == 1:
                        inicio_aprendiz = reverse('aprendiz:inicio_aprendiz')
                        login(request, user)
                        return redirect(inicio_aprendiz)
                    if rol.id_rol == 2:
                        inicio_instructor = reverse('instructor:inicio_instructor')
                        login(request, user)
                        return redirect(inicio_instructor)
                    if rol.id_rol == 3:
                        inicio_coordinacion = reverse('coordinacion:inicio_coordinacion')
                        login(request, user)
                        return redirect(inicio_coordinacion)
                    else:
                        messages.warning(request, 'No ha podido Iniciar Sesión')
                except UserProfile.DoesNotExist:
                    messages.warning(request, 'Perfil de usuario no encontrado')
            else:
                messages.warning(request, 'Credenciales inválidas')
        return render(request, 'users/login.html', {'title': 'Identifícate'})
def logout_user(request):
        logout(request)
        return redirect('inicio_usuarios')

@login_required(login_url="login")
def usuario(request, numeroiden, correo):
    usuario = authenticate(request, numeroiden=numeroiden, contraseña=contraseña)
    return render(request, "vistas/inicio.html",{
        'usuario' : usuario
    })
def crearsoli_usuario(request):
    detallesolicitud= Detallesolicitud.objects.all()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        form_detallesolicitud = DetalleSolicitudForm(request.POST)
        tipodocumentoform = TipoDocumentoForm(request.POST)
        if form_detallesolicitud.is_valid() and register_form.is_valid() and tipodocumentoform.is_valid():
            form_detallesolicitud.save()
            user = register_form.save()
            return render(request,'vistas/soli_usuarios.html')
    else:
        form_detallesolicitud = DetalleSolicitudForm()
        register_form = RegisterForm()
    tipodoc = Tipodocumento.objects.all()
    return render(request, 'vistas/soli_usuarios.html', {'form_detallesolicitud': form_detallesolicitud, 'detallesolicitud': detallesolicitud,
        'register_form': register_form,
        'tipodoc': tipodoc
        })

def eliminartiposoli_usuario(request, id_detallesolicitud):
    detallesolicitud = Detallesolicitud.objects.get(id_detallesolicitud=id_detallesolicitud)
    detallesolicitud.delete()
    return redirect('inicio_usuarios')