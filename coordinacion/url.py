
from django.urls import path, include
from coordinacion import views
from .views import actualizarperfil

app_name = 'coordinacion'
urlpatterns = [
    path('inicio-coordinacion/', views.inicio_coordinacion, name= "inicio_coordinacion"),
    path('noticias/', views.noticias, name="noticias"),
    path('actualizarperfil/', views.actualizarperfil, name='actualizarperfil'),


    
]