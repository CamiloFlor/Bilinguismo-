from django.db import models


# Create your models here.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)



class Calificacion(models.Model):
    id_califi = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calificacion'


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Competencia(models.Model):
    id_competencia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competencia'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estadoxinstru(models.Model):
    id_estadoxinstru = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    fecha_suspe = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadoxinstru'


class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    ficha = models.IntegerField(blank=True, null=True)
    id_programaformacion = models.ForeignKey('Programaformacion', models.DO_NOTHING, db_column='id_programaformacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ficha'


class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genero'


class Jornada(models.Model):
    id_jornada = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jornada'


class Mcer(models.Model):
    id_mcer = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mcer'


class Modalidad(models.Model):
    id_modalidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modalidad'


class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    id_poblacion = models.ForeignKey('Poblacion', models.DO_NOTHING, db_column='id_poblacion', blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    id_sector = models.ForeignKey('Sector', models.DO_NOTHING, db_column='id_sector', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipio'


class Nivelformacion(models.Model):
    id_nivel_formacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nivelformacion'


class Poblacion(models.Model):
    id_poblacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poblacion'


class Programaformacion(models.Model):
    id_programaformacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    id_competencia = models.ForeignKey(Competencia, models.DO_NOTHING, db_column='id_competencia', blank=True, null=True)
    id_nivel_formacion = models.ForeignKey(Nivelformacion, models.DO_NOTHING, db_column='id_nivel_formacion', blank=True, null=True)
    id_mcer = models.ForeignKey(Mcer, models.DO_NOTHING, db_column='id_mcer', blank=True, null=True)
    id_jornada = models.ForeignKey(Jornada, models.DO_NOTHING, db_column='id_jornada', blank=True, null=True)
    id_modalidad = models.ForeignKey(Modalidad, models.DO_NOTHING, db_column='id_modalidad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programaformacion'


class Resultadosaprendizaje(models.Model):
    id_resultado_aprendizaje = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    id_competencia = models.ForeignKey(Competencia, models.DO_NOTHING, db_column='id_competencia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resultadosaprendizaje'


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class Sector(models.Model):
    id_sector = models.AutoField(primary_key=True)
    barrio = models.CharField(db_column='Barrio', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comuna = models.CharField(db_column='Comuna', max_length=200, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sector'


class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_tpestado = models.ForeignKey('Tpestado', models.DO_NOTHING, db_column='id_tpestado', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    id_tpsoli = models.ForeignKey('Tiposolicitud', models.DO_NOTHING, db_column='id_tpsoli', blank=True, null=True)
    id_califi = models.ForeignKey(Calificacion, models.DO_NOTHING, db_column='id_califi', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud'


class Tipodocumento(models.Model):
    id_doc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipodocumento'


class Tiposolicitud(models.Model):
    id_tpsoli = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    archivo = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=150, blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    id_programaformacion = models.ForeignKey(Programaformacion, models.DO_NOTHING, db_column='id_programaformacion', blank=True, null=True)
    id_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)
    id_modalidad = models.ForeignKey(Modalidad, models.DO_NOTHING, db_column='id_modalidad', blank=True, null=True)
    id_ficha = models.ForeignKey(Ficha, models.DO_NOTHING, db_column='id_ficha', blank=True, null=True)
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    id_jornada = models.ForeignKey(Jornada, models.DO_NOTHING, db_column='id_jornada', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiposolicitud'


class Tpestado(models.Model):
    id_tpestado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpestado'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    numeroiden = models.IntegerField(blank=True, null=True)
    id_iden = models.ForeignKey(Tipodocumento, models.DO_NOTHING, db_column='id_iden', blank=True, null=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    id_ficha = models.ForeignKey(Ficha, models.DO_NOTHING, db_column='id_ficha', blank=True, null=True)
    nombre2 = models.CharField(max_length=30, blank=True, null=True)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    apellido2 = models.CharField(max_length=30, blank=True, null=True)
    id_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol', blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    correo1 = models.CharField(max_length=50, blank=True, null=True)
    contraseña = models.CharField(max_length=128, blank=True, null=True)
    id_genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_genero', blank=True, null=True)
    id_poblacion = models.ForeignKey(Poblacion, models.DO_NOTHING, db_column='id_poblacion', blank=True, null=True)
    id_estadoxinstru = models.ForeignKey(Estadoxinstru, models.DO_NOTHING, db_column='id_estadoxinstru', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'


