from django.contrib import admin
from .models import AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Calificacion, Categoria, Competencia, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, Estadoxinstru, Ficha, Genero, Jornada, Mcer, Modalidad, Municipio, Nivelformacion, Poblacion, Programaformacion, Resultadosaprendizaje, Rol, Sector, Solicitud, Tipodocumento, Tiposolicitud, Tpestado, Usuarios

class AuthGroupAdmin(admin.ModelAdmin):
    list_display = ['name']

class AuthGroupPermissionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'group', 'permission']

class AuthPermissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'content_type', 'codename']

class AuthUserAdmin(admin.ModelAdmin):
    list_display = ['password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined']

class AuthUserGroupsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'group']

class AuthUserUserPermissionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'permission']

class CalificacionAdmin(admin.ModelAdmin):
    list_display = ['id_califi', 'id_usuario']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_categoria', 'nombre']

class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ['id_competencia', 'nombre']

class DjangoAdminLogAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'object_id', 'object_repr', 'action_flag', 'change_message', 'content_type', 'user']

class DjangoContentTypeAdmin(admin.ModelAdmin):
    list_display = ['app_label', 'model']

class DjangoMigrationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'app', 'name', 'applied']

class DjangoSessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'session_data', 'expire_date']

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

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['id_municipio', 'id_poblacion', 'nombre', 'id_sector']

class NivelformacionAdmin(admin.ModelAdmin):
    list_display = ['id_nivel_formacion', 'nombre']

class PoblacionAdmin(admin.ModelAdmin):
    list_display = ['id_poblacion', 'nombre']

class ProgramaformacionAdmin(admin.ModelAdmin):
    list_display = ['id_programaformacion', 'nombre', 'id_competencia', 'id_nivel_formacion', 'id_mcer', 'id_jornada', 'id_modalidad']

class ResultadosaprendizajeAdmin(admin.ModelAdmin):
    list_display = ['id_resultado_aprendizaje', 'nombre', 'id_competencia']

class RolAdmin(admin.ModelAdmin):
    list_display = ['id_rol', 'nombre']

class SectorAdmin(admin.ModelAdmin):
    list_display = ['id_sector', 'barrio', 'comuna', 'direccion']

class SolicitudAdmin(admin.ModelAdmin):
    list_display = ['id_solicitud', 'id_usuario', 'id_tpestado', 'fecha_creacion', 'id_tpsoli', 'id_califi']

class TipodocumentoAdmin(admin.ModelAdmin):
    list_display = ['id_doc', 'nombre']

class TiposolicitudAdmin(admin.ModelAdmin):
    list_display = ['id_tpsoli', 'nombre', 'descripcion', 'archivo', 'url', 'fecha_fin', 'fecha_inicio', 'id_programaformacion', 'id_municipio', 'id_modalidad', 'id_ficha', 'id_categoria', 'id_jornada']

class TpestadoAdmin(admin.ModelAdmin):
    list_display = ['id_tpestado', 'nombre']

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ['id_usuario', 'numeroiden', 'id_iden', 'nombre', 'id_ficha', 'nombre2', 'apellido', 'apellido2', 'id_municipio', 'id_rol', 'celular', 'correo', 'correo1', 'contraseña', 'id_genero', 'id_poblacion', 'id_estadoxinstru']
    

admin.site.register(AuthGroup, AuthGroupAdmin)
admin.site.register(AuthGroupPermissions, AuthGroupPermissionsAdmin)
admin.site.register(AuthPermission, AuthPermissionAdmin)
admin.site.register(AuthUser, AuthUserAdmin)
admin.site.register(AuthUserGroups, AuthUserGroupsAdmin)
admin.site.register(AuthUserUserPermissions, AuthUserUserPermissionsAdmin)
admin.site.register(Calificacion, CalificacionAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(DjangoAdminLog, DjangoAdminLogAdmin)
admin.site.register(DjangoContentType, DjangoContentTypeAdmin)
admin.site.register(DjangoMigrations, DjangoMigrationsAdmin)
admin.site.register(DjangoSession, DjangoSessionAdmin)
admin.site.register(Estadoxinstru, EstadoxinstruAdmin)
admin.site.register(Ficha, FichaAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Jornada, JornadaAdmin)
admin.site.register(Mcer, McerAdmin)
admin.site.register(Modalidad, ModalidadAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Nivelformacion, NivelformacionAdmin)
admin.site.register(Poblacion, PoblacionAdmin)
admin.site.register(Programaformacion, ProgramaformacionAdmin)
admin.site.register(Resultadosaprendizaje, ResultadosaprendizajeAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Tipodocumento, TipodocumentoAdmin)
admin.site.register(Tiposolicitud, TiposolicitudAdmin)
admin.site.register(Tpestado, TpestadoAdmin)
admin.site.register(Usuarios, UsuariosAdmin)
