from django.contrib import admin                                                             # Importing necessary modules and functions
from django.urls import path, include
from aprendiz import views
app_name = 'aprendiz'                                                                       # Declaring the app name for namespacing URLs
urlpatterns = [                                                                             # Defining URL patterns for the app
    path('Inicio-Aprendiz/', views.inicio_aprendiz, name="inicio_aprendiz"),                # URL pattern for the "inicio_aprendiz" view
    path('Solicitud/', views.crearsoli, name="crearsoli"),                                  # URL pattern for the "crearsoli" view
    path('Solicitud-eliminar/<int:id_detallesolicitud>', views.eliminar_tiposolicitud, name="eliminar_tiposolicitud"),  # URL pattern for the "eliminar_tiposolicitud" view
]
