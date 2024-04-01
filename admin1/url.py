from django.contrib import admin
from django.urls import path
from django.urls import path, include
from admin1 import views
from . import views

urlpatterns = [
    path('',views.inicio, name="inicio"),
    path('Solicitud/', views.crearsoli, name="crearsoli"),
    path('noticias/', views.noticias, name="noticias")
    

]