from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from usuarios.forms import RegisterForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from usuarios.models import Rol,Solicitud, UserProfile, Detallesolicitud, Tipodocumento, TipoSolicitud, Municipios, Departamentos, Poblados
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
    if request.method == 'POST':
            # Obtener los datos del formulario
            cod_dpto = request.POST.get('cod_dpto')
            cod_municipio = request.POST.get('cod_municipio')
            cod_poblado = request.POST.get('cod_poblado')
            descripcion = request.POST.get('descripcion')
            direccion = request.POST.get('direccion')
            id_tipodoc = request.POST.get('id_doc')  # Tipo de documento del usuario
            id_tiposolicitud = request.POST.get('id_tiposolicitud')
            fecha_inicio = request.POST.get('fecha_inicio')
            archivo = request.FILES.get('archivo')
            id_programaformacion = request.POST.get('id_programaformacion')

            # Crear instancias de los modelos y asignar los valores
            userprofile = UserProfile.objects.create(
                user=user,
                cod_dpto=cod_dpto,
                cod_municipio=cod_municipio,
                cod_poblado=cod_poblado,
                direccion=direccion,
                id_doc=id_tipodoc,  # Asignar el tipo de documento
            )
            if userprofile.id_doc == 3:
                userprofile.id_rol = 4
            userprofile.save()

            detallesolicitud = Detallesolicitud.objects.create(
                id_tiposolicitud=id_tiposolicitud,
                descripcion=descripcion,
                fecha_inicio=fecha_inicio,
                archivo=archivo,
                id_programaformacion=id_programaformacion,
            )
            detallesolicitud.save()
            Solicitud = Solicitudes.objects.create(
                user=user
            )

            return render(request, 'users/login.html')
    else:
        register_form = RegisterForm()
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

def eliminartiposoli_usuario(request, id_detallesolicitud):
    detallesolicitud = Detallesolicitud.objects.get(id_detallesolicitud=id_detallesolicitud)
    detallesolicitud.delete()
    return redirect('inicio_usuarios')