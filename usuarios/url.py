from django.contrib import admin
from django.urls import path, include
from usuarios import views
app_name = 'usuarios'
urlpatterns=[
    path('Login/', views.login_user, name="login_user"),
    path('Registro/', views.registro, name="registro"),
    path('Logout/', views.logout_user, name="logout"),
    path('Solicitud/', views.crearsoli_usuario, name="crearsoli_usuario"),
    path('Solicitud-eliminar/<int:id_detallesolicitud>', views.eliminartiposoli_usuario, name="eliminartiposoli_usuario"),
]
