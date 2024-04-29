from django.contrib import admin
from .models import  Calificacion, Categoria, Competencia, Estadoxinstru, Ficha, Genero, Jornada, Mcer, Modalidad, Nivelformacion, Programaformacion, Resultadosaprendizaje, Rol,  Solicitud, Tipodocumento, TipoSolicitud, Detallesolicitud, Tpestado, UserProfile

class CalificacionAdmin(admin.ModelAdmin):
    list_display = ['id_calificacion', 'user']

class DetallesolicitudAdmin(admin.ModelAdmin):
    list_display = ['id_detallesolicitud',  'id_tiposolicitud', 'descripcion', 'archivo', 'url', 'fecha_fin', 'fecha_inicio', 'id_programaformacion', 'id_modalidad', 'id_ficha', 'id_categoria', 'id_jornada']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_categoria', 'nombre']

class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ['id_competencia', 'nombre']

class EstadoxinstruAdmin(admin.ModelAdmin):
    list_display = ['id_estadoxinstru', 'nombre', 'fecha_suspe']

class FichaAdmin(admin.ModelAdmin):
    list_display = ['id_ficha', 'ficha', 'id_programaformacion']

class GeneroAdmin(admin.ModelAdmin):
    list_display = ['id_genero', 'nombre']

class JornadaAdmin(admin.ModelAdmin):
    list_display = ['id_jornada', 'nombre']

class McerAdmin(admin.ModelAdmin):
    list_display = ['id_mcer', 'nombre']

class ModalidadAdmin(admin.ModelAdmin):
    list_display = ['id_modalidad', 'nombre']

class NivelformacionAdmin(admin.ModelAdmin):
    list_display = ['id_nivel_formacion', 'nombre']


class ProgramaformacionAdmin(admin.ModelAdmin):
    list_display = ['id_programaformacion', 'nombre', 'id_competencia', 'id_nivel_formacion', 'id_mcer', 'id_jornada', 'id_modalidad']

class ResultadosaprendizajeAdmin(admin.ModelAdmin):
    list_display = ['id_resultado_aprendizaje', 'nombre', 'id_competencia']

class RolAdmin(admin.ModelAdmin):
    list_display = ['id_rol', 'nombre']


class SolicitudAdmin(admin.ModelAdmin):
    list_display = ['id_solicitud', 'user', 'id_tpestado', 'fecha_creacion', 'id_detallesolicitud', 'id_calificacion']

class TipodocumentoAdmin(admin.ModelAdmin):
    list_display = ['id_doc', 'nombre']

class TipoSolicitudAdmin(admin.ModelAdmin):
    list_display = ['id_tiposolicitud', 'nombre' ]

class TpestadoAdmin(admin.ModelAdmin):
    list_display = ['id_tpestado', 'nombre']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id_userprofile', 'numeroiden', 'id_doc', 'nombre', 'id_ficha', 'nombre2', 'apellido', 'apellido2', 'id_rol', 'celular', 'correo', 'correo1', 'id_genero', 'id_estadoxinstru']


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