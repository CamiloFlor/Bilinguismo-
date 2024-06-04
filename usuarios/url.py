from django.contrib import admin
from django.urls import path                                                     # Importa el módulo admin de Django para registrar modelos y gestionar el panel de administración.
from django.urls import path, include                                                # Importa las funciones path y include del módulo urls de Django. 
from usuarios import views                                                           # Importa las vistas definidas en la aplicación 'usuarios'.
app_name = 'usuarios'                                                                # Establece el espacio de nombres de la aplicación como 'usuarios'.
urlpatterns = [                                                                      # Define las rutas de la aplicación 'usuarios'.  
    path('Login/', views.login_user, name="login_user"),                             # Ruta para la vista de inicio de sesión de usuario.
    path('Registro/', views.registro, name="registro"),                              # Ruta para la vista de registro de usuario.
    path('Logout/', views.logout_user, name="logout"),                               # Ruta para la vista de cierre de sesión de usuario.
    path('Solicitud/', views.crearsoli_usuario, name="crearsoli_usuario"),           # Ruta para la vista de creación de solicitud de usuario.
    path('get_municipios/', views.get_municipios, name="municipios"),                # Ruta para la vista que devuelve los municipios en función de una solicitud AJAX.
    path('get_poblados/', views.get_poblados, name="poblados"),                      # Ruta para la vista que devuelve los poblados en función de una solicitud AJAX.
    path('Solicitud-eliminar/<int:id_detallesolicitud>', views.eliminartiposoli_usuario, name="eliminartiposoli_usuario"),   # Ruta para la vista de eliminación de tipos de solicitud de usuario.
]