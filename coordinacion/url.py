<<<<<<< HEAD

from django.urls import path, include
from coordinacion import views
app_name = 'coordinacion'
urlpatterns = [
    path('inicio-coordinacion/', views.inicio_coordinacion, name= "inicio_coordinacion"),
    path('noticias/', views.noticias, name="noticias"),
]
=======
                                                                                                    # Importación de las funciones y clases necesarias desde los módulos de Django y la aplicación coordinacion
from django.urls import path, include
from coordinacion import views
from .views import actualizarperfil, gestiondepermisos
                                                                                                    # Establecimiento del espacio de nombres de la aplicación
app_name = 'coordinacion'
                                                                                                    # Definición de las URL de la aplicación
urlpatterns = [
      path('inicio-coordinacion/', views.inicio_coordinacion, name="inicio_coordinacion"),          # Ruta para la vista de inicio de coordinación
      path('noticias/', views.noticias, name="noticias"),                                           # Ruta para la vista de noticias
      path('actualizarperfil/', views.actualizarperfil, name='actualizarperfil'),                   # Ruta para la vista de actualización de perfil
      path('gestiondepermisos/', views.gestiondepermisos, name='gestiondepermisos'),                # Ruta para la vista de gestión de permisos
]
>>>>>>> 9dbd9c1b52866ecd1ff328aa990b020db312123f
