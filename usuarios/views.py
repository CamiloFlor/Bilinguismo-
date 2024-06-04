from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from usuarios.forms import RegisterForm, UserProfileForm, DetalleSolicitudForm, TipoDocumentoForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from usuarios.models import Rol, UserProfile, Detallesolicitud, Tipodocumento, Municipios, TipoSolicitud
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
    municipio = Municipio.objects.all()
    detallesolicitud= Detallesolicitud.objects.all()
    tiposoli = TipoSolicitud.objects.all()
    tipodoc = Tipodocumento.objects.all()
    return render(request, 'vistas/soli_usuarios.html', {'form_detallesolicitud': form_detallesolicitud, 'detallesolicitud': detallesolicitud,
        'register_form': register_form,
        'tipodoc': tipodoc,
        'municipio': municipio,
        'tiposoli': tiposoli
        })

def eliminartiposoli_usuario(request, id_detallesolicitud):
    detallesolicitud = Detallesolicitud.objects.get(id_detallesolicitud=id_detallesolicitud)
    detallesolicitud.delete()
    return redirect('inicio_usuarios')
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
                                                                                                                # Define una vista llamada "inicio_usuarios" que devuelve una plantilla HTML 'inicio.html'
                                                                                                                # con el contexto que contiene el título de la ventana.
def inicio_usuarios(request):
    return render(request, 'vistas/inicio.html', {
        # 'tituloventana': "Inicio"
    })
                                                                                                                # Define una vista llamada "get_municipios" que responde a las solicitudes AJAX GET.
                                                                                                                # Filtra los municipios según el departamento proporcionado en la solicitud y los devuelve como JSON.
                                                                                                                # Si no se proporciona el parámetro 'departamento' en la solicitud, devuelve un error 400.
def get_municipios(request):
    if request.method == 'GET' and 'departamento' in request.GET:
        departamento = request.GET['departamento']
        municipios = Municipios.objects.filter(cod_dpto=departamento).values('cod_municipio', 'nombre_municipio')
        return JsonResponse(list(municipios), safe=False)
    else:
        return JsonResponse({'error': 'Se requiere un parámetro "departamento" '}, status=400)
                                                                                                                # Define una vista llamada "get_poblados" que responde a las solicitudes AJAX GET.
                                                                                                                # Filtra los poblados según el municipio proporcionado en la solicitud y los devuelve como JSON.
                                                                                                                # Si no se proporciona el parámetro 'municipios' en la solicitud, devuelve un error 400.
def get_poblados(request):
    if request.method == 'GET' and 'municipios' in request.GET:
        municipios = request.GET['municipios']
        poblado = Poblados.objects.filter(cod_municipio=municipios).values('cod_poblado', 'nombre_poblado')
        return JsonResponse(list(poblado), safe=False)
    else:
        return JsonResponse({'error': 'Se requiere un parámetro "Municipio" '}, status=400)

                                                                                                                # Define una vista llamada "registro" que maneja el registro de usuarios.
                                                                                                                # Si la solicitud es POST, valida los formularios de registro y de perfil de usuario.
                                                                                                                # Si ambos son válidos, crea un nuevo usuario y su perfil asociado, asigna el rol seleccionado y redirige a la página de inicio.
                                                                                                                # Si la solicitud no es POST, muestra los formularios de registro y perfil de usuario vacíos.
                                                                                                                # Además, carga todos los roles disponibles para mostrar en el formulario.
def registro(request):
    if request.method == 'POST':
                                                                                                                # Crea instancias de los formularios de registro y de perfil de usuario con los datos de la solicitud POST.
        register_form = RegisterForm(request.POST)
        userprofile_form = RolForm(request.POST)
                                                                                                                # Verifica si ambos formularios son válidos.
        if register_form.is_valid() and userprofile_form.is_valid():
                                                                                                                # Guarda el usuario creado por el formulario de registro.
            user = register_form.save()
                                                                                                                # Guarda el perfil de usuario, pero no lo guarda en la base de datos todavía.
            user_profile = userprofile_form.save(commit=False)
                                                                                                                # Asigna el usuario al perfil de usuario.
            user_profile.user = user
                                                                                                                # Asigna el rol seleccionado en el formulario al perfil de usuario.
            user_profile.id_rol = userprofile_form.cleaned_data['id_rol']
                                                                                                                # Guarda el perfil de usuario en la base de datos.
            user_profile.save()
                                                                                                                # Muestra un mensaje de advertencia sobre el éxito del registro.
            messages.warning(request, 'registro EXITOSO !!!')
                                                                                                                # Redirige a la página de inicio.
            return redirect('inicio_usuarios')
    else:
                                                                                                                 # Si la solicitud no es POST, crea instancias de los formularios de registro y de perfil de usuario vacíos.
        register_form = RegisterForm()
        userprofile_form = RolForm()
                                                                                                                # Obtiene todos los roles disponibles desde la base de datos.
    roles = Rol.objects.all()
                                                                                                                # Renderiza la plantilla de registro con los formularios y los roles disponibles.
    return render(request, 'users/registro.html', {
        'title': 'Registro',
        'roles': roles,
        'register_form': register_form,
        'userprofile_form': userprofile_form,
    })

                                                                                                                # Define una vista llamada "login_user" que maneja el inicio de sesión de usuarios.
                                                                                                                # Si el usuario ya está autenticado, redirige a la página de inicio de usuarios.
                                                                                                                # Si la solicitud es POST, intenta autenticar al usuario utilizando las credenciales proporcionadas.
                                                                                                                # Dependiendo del rol del usuario autenticado, redirige a la página correspondiente.
                                                                                                                # Si el usuario no está autenticado o las credenciales son inválidas, muestra un mensaje de advertencia.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('inicio_usuarios')
    else:
        if request.method == 'POST':
                                                                                                                # Obtiene el nombre de usuario y la contraseña proporcionados en la solicitud POST.
            username = request.POST.get('username')
            password = request.POST.get('password')
                                                                                                                # Autentica al usuario utilizando las credenciales proporcionadas.
            user = authenticate(request, username=username, password=password)
                                                                                                                # Verifica si el usuario es autenticado correctamente.
            if user is not None:
                try:
                                                                                                                # Obtiene el perfil de usuario asociado al usuario autenticado.
                    user_profile = UserProfile.objects.get(user=user)
                                                                                                                # Obtiene el rol del usuario.
                    rol = user_profile.id_rol                                                                                                                # Redirige a la página correspondiente según el rol del usuario.
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
                                                                                                                 # Si la solicitud no es POST, muestra el formulario de inicio de sesión.
        return render(request, 'users/login.html', {'title': 'Identifícate'})

                                                                                                                # Define una vista llamada "logout_user" que maneja el cierre de sesión de usuarios.
                                                                                                                # Cierra la sesión del usuario y redirige a la página de inicio de usuarios.
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
                                                                                                                    
                                                                                                                # Define una vista llamada "crearsoli_usuario" que maneja la creación de solicitudes de usuario.
                                                                                                                # Si la solicitud es POST, procesa los datos del formulario de solicitud y crea una nueva solicitud de usuario.
                                                                                                                # Si todos los formularios son válidos, guarda el usuario y su perfil asociado, crea una nueva solicitud y guarda los detalles de la solicitud.
                                                                                                                # Además, realiza algunas operaciones relacionadas con los perfiles de usuario y los roles.
                                                                                                                # Si la solicitud no es POST, muestra los formularios de registro de usuario, documento y tipo de solicitud.
def crearsoli_usuario(request):
    if request.method == 'POST':
                                                                                                                # Crear instancias de los formularios de registro de usuario, documento y tipo de solicitud con los datos de la solicitud POST.
        register_form = RegisterForm(request.POST)
        docform = DocForm(request.POST)
        tiposoli = TipoSoliForm(request.POST)
                                                                                                                # Obtener otros datos de la solicitud POST.
        direccion = request.POST.get('direccion')
        cod_dpto = request.POST.get('cod_dpto')
        cod_municipio = request.POST.get('cod_municipio')
        cod_poblado = int(request.POST.get('cod_poblado'))
        descripcion = request.POST.get('descripcion')
        fecha_inicio_str = request.POST.get('fecha_inicio')
        archivo = request.FILES.get('archivo', None)
                                                                                                                # Convertir la fecha de inicio a formato de fecha.
        if fecha_inicio_str:
            fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')
        else:
            fecha_inicio = None
                                                                                                                # Verificar si todos los formularios son válidos.
        if register_form.is_valid() and docform.is_valid() and tiposoli.is_valid():
                                                                                                                # Guardar el usuario creado por el formulario de registro.
            user = register_form.save()  
                                                                                                                # Guardar el documento del usuario.
            doc_form = docform.save(commit=False)
                                                                                                                # Guardar el tipo de solicitud.
            tipo_soli = tiposoli.save(commit=False)
                                                                                                                # Obtener objetos relacionados con ubicación (departamento, municipio, poblado).
            departamento = Departamentos.objects.get(cod_dpto=cod_dpto)
            municipio = Municipios.objects.get(cod_municipio=cod_municipio)
            poblado = Poblados.objects.get(cod_poblado=cod_poblado)
                                                                                                                # Crear o recuperar el perfil de usuario asociado al usuario.
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.id_doc = docform.cleaned_data['id_doc']
            user_profile.direccion = direccion
            user_profile.cod_dpto = departamento
            user_profile.cod_municipio = municipio
            user_profile.cod_poblado = poblado
            user_profile.save()
                                                                                                                # Actualizar el rol del usuario si el tipo de documento es igual a 3.
            if user_profile.id_doc == 3:
                user_profile.id_rol = 4
                user_profile.save()
                                                                                                                # Crear una nueva instancia de DetalleSolicitud.
            detalle_soli, created = Detallesolicitud.objects.get_or_create(
                id_tiposolicitud=tiposoli.cleaned_data['id_tiposolicitud'],
                descripcion=descripcion,
                fecha_inicio=fecha_inicio,
                archivo=archivo,
            )
            detalle_soli.save()
                                                                                                                # Crear una nueva instancia de Solicitud asociada al usuario y al detalle de solicitud.
            soli = Solicitud.objects.create(
                user=user,
                id_detallesolicitud=detalle_soli
            )
            soli.save()
        else:
                                                                                                                # Si algún formulario no es válido, crear instancias vacías de los formularios.
            register_form = RegisterForm()
            docform = DocForm()
            tiposoli = TipoSoliForm()
    else:
                                                                                                                # Si la solicitud no es POST, crear instancias vacías de los formularios.
        register_form = RegisterForm()
        docform = DocForm()
        tiposoli = TipoSoliForm()
                                                                                                                # Obtener todos los detalles de solicitud, tipos de solicitud, tipos de documento y ubicaciones disponibles.
    detallesolicitud = Detallesolicitud.objects.all()
    tiposoli = TipoSolicitud.objects.all()
    tipodoc = Tipodocumento.objects.all()
    depto = Departamentos.objects.all()
                                                                                                                # Renderizar la plantilla de creación de solicitud con los datos necesarios.
    return render(request, 'vistas/soli_usuarios.html', {
        'detallesolicitud': detallesolicitud,
        'register_form': register_form,
        'tipodoc': tipodoc,
        'tiposoli': tiposoli,
        'depto': depto
    })
                                                                                                                # Define una vista llamada "eliminartiposoli_usuario" que maneja la eliminación de detalles de solicitud de usuario.
                                                                                                                # Recibe el ID del detalle de solicitud a eliminar como parámetro.
                                                                                                                # Busca el detalle de solicitud correspondiente en la base de datos y lo elimina.
                                                                                                                # Luego, redirige a la página de inicio de usuarios.
def eliminartiposoli_usuario(request, id_detallesolicitud):
                                                                                                                # Busca el detalle de solicitud en la base de datos por su ID.
    detallesolicitud = Detallesolicitud.objects.get(id_detallesolicitud=id_detallesolicitud)
                                                                                                                # Elimina el detalle de solicitud.
    detallesolicitud.delete()
                                                                                                                # Redirige a la página de inicio de usuarios.
    return redirect('inicio_usuarios')


