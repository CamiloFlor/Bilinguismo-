# Importa el administrador de Django.
from django.contrib import admin
# Importa los modelos desde el directorio actual.
from .models import Calificacion, Categoria, Competencia, Estadoxinstru, Ficha, Genero, Jornada, Mcer, Modalidad, Nivelformacion, Programaformacion, Resultadosaprendizaje, Rol, Solicitud, Tipodocumento, TipoSolicitud, Detallesolicitud, Tpestado, UserProfile
# Define una clase de administración para el modelo Calificacion.
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ['id_calificacion', 'user']
# Define una clase de administración para el modelo Detallesolicitud.
class DetallesolicitudAdmin(admin.ModelAdmin):
    list_display = ['id_detallesolicitud', 'id_tiposolicitud', 'descripcion', 'archivo', 'url', 'fecha_fin', 'fecha_inicio', 'id_programaformacion', 'id_modalidad', 'id_ficha', 'id_categoria', 'id_jornada']
# Define una clase de administración para el modelo Categoria.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_categoria', 'nombre']
# Define una clase de administración para el modelo Competencia.
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ['id_competencia', 'nombre']
# Define una clase de administración para el modelo Estadoxinstru.
class EstadoxinstruAdmin(admin.ModelAdmin):
    list_display = ['id_estadoxinstru', 'nombre', 'fecha_suspe']
# Define una clase de administración para el modelo Ficha.
class FichaAdmin(admin.ModelAdmin):
    list_display = ['id_ficha', 'ficha', 'id_programaformacion']
# Define una clase de administración para el modelo Genero.
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['id_genero', 'nombre']
# Define una clase de administración para el modelo Jornada.
class JornadaAdmin(admin.ModelAdmin):
    list_display = ['id_jornada', 'nombre']
# Define una clase de administración para el modelo Mcer.
class McerAdmin(admin.ModelAdmin):
    list_display = ['id_mcer', 'nombre']
# Define una clase de administración para el modelo Modalidad.
class ModalidadAdmin(admin.ModelAdmin):
    list_display = ['id_modalidad', 'nombre']
# Define una clase de administración para el modelo Nivelformacion.
class NivelformacionAdmin(admin.ModelAdmin):
    list_display = ['id_nivel_formacion', 'nombre']
# Define una clase de administración para el modelo Programaformacion.
class ProgramaformacionAdmin(admin.ModelAdmin):
    list_display = ['id_programaformacion', 'nombre', 'id_competencia', 'id_nivel_formacion', 'id_mcer', 'id_jornada', 'id_modalidad']
# Define una clase de administración para el modelo Resultadosaprendizaje.
class ResultadosaprendizajeAdmin(admin.ModelAdmin):
    list_display = ['id_resultado_aprendizaje', 'nombre', 'id_competencia']
# Define una clase de administración para el modelo Rol.
class RolAdmin(admin.ModelAdmin):
    list_display = ['id_rol', 'nombre']
# Define una clase de administración para el modelo Solicitud.
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ['id_solicitud', 'user', 'id_tpestado', 'fecha_creacion', 'id_detallesolicitud', 'id_calificacion']
# Define una clase de administración para el modelo Tipodocumento.
class TipodocumentoAdmin(admin.ModelAdmin):
    list_display = ['id_doc', 'nombre']
# Define una clase de administración para el modelo TipoSolicitud.
class TipoSolicitudAdmin(admin.ModelAdmin):
    list_display = ['id_tiposolicitud', 'nombre']
# Define una clase de administración para el modelo Tpestado.
class TpestadoAdmin(admin.ModelAdmin):
    list_display = ['id_tpestado', 'nombre']
# Define una clase de administración para el modelo UserProfile.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id_userprofile', 'numeroiden', 'id_doc', 'nombre', 'id_ficha', 'nombre2', 'apellido', 'apellido2', 'id_rol', 'celular', 'correo', 'correo1', 'id_genero', 'id_estadoxinstru']
# Registra los modelos junto con sus clases de administración personalizadas en el panel de administración.

admin.site.register(Calificacion, CalificacionAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Estadoxinstru, EstadoxinstruAdmin)
admin.site.register(Ficha, FichaAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Jornada, JornadaAdmin)
admin.site.register(Mcer, McerAdmin)
admin.site.register(Modalidad, ModalidadAdmin)

admin.site.register(Nivelformacion, NivelformacionAdmin)
admin.site.register(Programaformacion, ProgramaformacionAdmin)
admin.site.register(Resultadosaprendizaje, ResultadosaprendizajeAdmin)
admin.site.register(Rol, RolAdmin)

admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Tipodocumento, TipodocumentoAdmin)
admin.site.register(TipoSolicitud, TipoSolicitudAdmin)
admin.site.register(Detallesolicitud, DetallesolicitudAdmin)
admin.site.register(Tpestado, TpestadoAdmin)

admin.site.register(UserProfile, UserProfileAdmin)

