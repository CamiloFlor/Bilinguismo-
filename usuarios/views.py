from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from usuarios.forms import RegisterForm, RolForm, DocForm, TipoSoliForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from usuarios.models import Rol,Solicitud, UserProfile, Detallesolicitud, Tipodocumento, TipoSolicitud, Municipios, Departamentos, Poblados
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime 

# Create your views here.

def inicio_usuarios(request):
    return render(request, 'vistas/inicio.html',{
        'tituloventana': "Inicio"
    })
def get_municipios(request):
    if request.method == 'GET' and 'departamento' in request.GET:
        departamento = request.GET['departamento']
        municipios = Municipios.objects.filter(cod_dpto=departamento).values('cod_municipio', 'nombre_municipio')
        return JsonResponse(list(municipios), safe=False)
    else:
        return JsonResponse({'error': 'Se requiere un parámetro "departamento" '}, status=400)
def get_poblados(request):
    if request.method == 'GET' and 'municipios' in request.GET:
        municipios = request.GET['municipios']
        poblado = Poblados.objects.filter(cod_municipio=municipios).values('cod_poblado', 'nombre_poblado')
        return JsonResponse(list(poblado), safe=False)
    else:
        return JsonResponse({'error': 'Se requiere un parámetro "Municipio" '}, status=400)
def registro(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        userprofile_form = RolForm(request.POST)
        if register_form.is_valid() and userprofile_form.is_valid():
            user = register_form.save()
            user_profile = userprofile_form.save(commit=False)
            user_profile.user = user
            user_profile.id_rol = userprofile_form.cleaned_data['id_rol']  # Asigna el id_rol seleccionado en el formulario
            user_profile.save()
            return redirect('inicio_usuarios')
    else:
        register_form = RegisterForm()
        userprofile_form = RolForm()
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

#def solicitud(id_detallesolicitud, user):
    


def crearsoli_usuario(request):
    if request.method == 'POST':
        # Crear el formulario de registro de usuario
        # USUARIO
        register_form = RegisterForm(request.POST)
        docform = DocForm(request.POST)
        tiposoli = TipoSoliForm(request.POST)
        direccion = request.POST.get('direccion')
        cod_dpto = request.POST.get('cod_dpto')
        cod_municipio = request.POST.get('cod_municipio')
        cod_poblado = int(request.POST.get('cod_poblado'))
        # SOLICITUD
        descripcion = request.POST.get('descripcion')
        fecha_inicio_str = request.POST.get('fecha_inicio')
        fecha_inicio_str = request.POST.get('fecha_inicio')
        archivo = request.FILES.get('archivo', None)
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')
        if register_form.is_valid() and docform.is_valid() and tiposoli.is_valid():
            #user 
            user = register_form.save()
            doc_form = docform.save(commit=False)
            tipo_soli=tiposoli.save(commit=False)
            #Perfil de Usuario
            departamento = Departamentos.objects.get(cod_dpto=cod_dpto)
            municipio = Municipios.objects.get(cod_municipio=cod_municipio)
            poblado = Poblados.objects.get(cod_poblado=cod_poblado)
            user_profile, created = UserProfile.objects.get_or_create(
                user=user,
                
            )
            user_profile.id_doc = docform.cleaned_data['id_doc']
            user_profile.direccion = direccion
            user_profile.cod_dpto = departamento
            user_profile.cod_municipio = municipio
            user_profile.cod_poblado = poblado
            user_profile.save()
            userprofile = UserProfile.objects.get(id_userprofile=user_profile) 
            if userprofile.id_doc == 3:
                userprofile.id_rol = 4
                user_profile.save()
            #Detalle Solicitud
            detalle_soli, created = Detallesolicitud.objects.get_or_create(
                id_tiposolicitud = tiposoli.cleaned_data['id_tiposolicitud'],
                descripcion = descripcion,
                fecha_inicio = fecha_inicio,
                archivo = archivo,
            )
            detalle_soli.save()
            #Solicitud(user)
            soli, created = Solicitud.objects.create(
            user=user,
            id_detallesolicitud=detalle_soli
            )
            soli.save()
            
            # SOLICITUD
            
            
        else:
            register_form = RegisterForm()
            docform = DocForm()
            tiposoli = TipoSoliForm()
    else:
        register_form = RegisterForm()
        docform = DocForm()
        tiposoli = TipoSoliForm()
    detallesolicitud = Detallesolicitud.objects.all()
    tiposoli = TipoSolicitud.objects.all()
    tipodoc = Tipodocumento.objects.all()
    depto = Departamentos.objects.all()
    return render(request, 'vistas/soli_usuarios.html', {
        'detallesolicitud': detallesolicitud,
        'register_form': register_form,
        'tipodoc': tipodoc,
        'tiposoli': tiposoli,
        'depto': depto
    })

def eliminartiposoli_usuario(request, id_detallesolicitud):
    detallesolicitud = Detallesolicitud.objects.get(id_detallesolicitud=id_detallesolicitud)
    detallesolicitud.delete()
    return redirect('inicio_usuarios')



