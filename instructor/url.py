from django.contrib import admin
from django.urls import path, include
from instructor import views
app_name = 'instructor'
urlpatterns = [
    path('inicio-instructor/', views.inicio_instructor, name= "inicio_instructor"),
    path('Solicitud/', views.crearsoli_instructor, name="crearsoli_instructor"),
    path('Solicitud-eliminar/<int:id_detallesolicitud>', views.eliminartiposoli_instructor, name="eliminartiposoli_instructor"),
<<<<<<< HEAD
    path('noti/', views.noti_instru, name='noti'),
    path('noti/crear/', views.crear_instru, name='crear'),
    path('noti/editar/', views.crear_instru, name='editar'),
    path('eliminar/<int:id>', views.eliminar_instru, name='eliminar'),
    path('noti/editar/<int:id>', views.editar_instru, name='editar'),
    
=======
>>>>>>> 9dbd9c1b52866ecd1ff328aa990b020db312123f
]
