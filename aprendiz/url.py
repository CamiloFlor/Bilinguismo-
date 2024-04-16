from django.contrib import admin
from django.urls import path, include
from aprendiz import views
app_name = 'aprendiz'
urlpatterns=[
    path('Inicio-Aprendiz/', views.inicio_aprendiz, name="inicio_aprendiz"),
    path('Solicitud/', views.crearsoli, name="crearsoli"),
    path('Solicitud-eliminar/<int:id_detallesolicitud>', views.eliminar_tiposolicitud, name="eliminar_tiposolicitud"),
]