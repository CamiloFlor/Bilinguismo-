from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estadoxinstru(models.Model):
    id_estadoxinstru = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    fecha_suspe = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed =  True
        db_table = 'estadoxinstru'


class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    ficha = models.IntegerField(blank=True, null=True)
    id_programaformacion = models.ForeignKey('Programaformacion', models.DO_NOTHING, db_column='id_programaformacion', blank=True, null=True)

    class Meta:
        managed =  True
        db_table = 'ficha'


class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed =  True
        db_table = 'genero'

class Competencia(models.Model):
    id_competencia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    class Meta:
        managed =  True
        db_table = 'Competencia'
class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    id_userprofile = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'calificacion'

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categoria'

class Jornada(models.Model):
    id_jornada = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed =  True
        db_table = 'jornada'


class Mcer(models.Model):
    id_mcer = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed =  True
        db_table = 'mcer'


class Modalidad(models.Model):
    id_modalidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed =  True
        db_table = 'modalidad'


class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    id_poblacion = models.ForeignKey('Poblacion', models.DO_NOTHING, db_column='id_poblacion', blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    id_sector = models.ForeignKey('Sector', models.DO_NOTHING, db_column='id_sector', blank=True, null=True)

    class Meta:
        managed =  True
        db_table = 'municipio'


class Nivelformacion(models.Model):
    id_nivel_formacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed =  True
        db_table = 'nivelformacion'


class Poblacion(models.Model):
    id_poblacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed =  True
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
        managed =  True
        db_table = 'programaformacion'


class Resultadosaprendizaje(models.Model):
    id_resultado_aprendizaje = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    id_competencia = models.ForeignKey(Competencia, models.DO_NOTHING, db_column='id_competencia', blank=True, null=True)

    class Meta:
        managed =  True
        db_table = 'resultadosaprendizaje'


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed =  True
        db_table = 'rol'


class Sector(models.Model):
    id_sector = models.AutoField(primary_key=True)
    barrio = models.CharField(db_column='Barrio', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comuna = models.CharField(db_column='Comuna', max_length=200, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sector'


class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    id_userprofile = models.ForeignKey('Userprofile', models.DO_NOTHING, db_column='id_userprofile', blank=True, null=True)
    id_tpestado = models.ForeignKey('Tpestado', models.DO_NOTHING, db_column='id_tpestado', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    id_detallesolicitud = models.ForeignKey('Detallesolicitud', models.DO_NOTHING, db_column='id_detallesolicitud', blank=True, null=True)
    id_calificacion = models.ForeignKey(Calificacion, models.DO_NOTHING, db_column='id_calificacion', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'solicitud'


class Tipodocumento(models.Model):
    id_doc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipodocumento'

class TipoSolicitud(models.Model):
    id_tiposolicitud = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TipoSolicitud'


class Detallesolicitud(models.Model):
    id_detallesolicitud = models.AutoField(primary_key=True)
    id_tiposolicitud = models.ForeignKey(TipoSolicitud, models.DO_NOTHING, db_column='id_tiposolicitud', blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    archivo = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    imagen = models.TextField(db_column='Imagen', blank=True, null=True)  # Field name made lowercase.
    fecha_fin = models.DateTimeField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    id_programaformacion = models.ForeignKey(Programaformacion, models.DO_NOTHING, db_column='id_programaformacion', blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    id_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)
    id_modalidad = models.ForeignKey(Modalidad, models.DO_NOTHING, db_column='id_modalidad', blank=True, null=True)
    id_ficha = models.ForeignKey(Ficha, models.DO_NOTHING, db_column='id_ficha', blank=True, null=True)
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    id_jornada = models.ForeignKey(Jornada, models.DO_NOTHING, db_column='id_jornada', blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detallesolicitud'

class Tpestado(models.Model):
    id_tpestado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tpestado'

class UserProfile(models.Model):
    id_userprofile = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    numeroiden = models.IntegerField(unique=True, blank=True, null=True)
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
    password = models.CharField(max_length=128, blank=True, null=True)
    id_genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_genero', blank=True, null=True)
    id_poblacion = models.ForeignKey(Poblacion, models.DO_NOTHING, db_column='id_poblacion', blank=True, null=True)
    id_estadoxinstru = models.ForeignKey(Estadoxinstru, models.DO_NOTHING, db_column='id_estadoxinstru', blank=True, null=True)
    class Meta:
        managed =  True
        db_table = 'UserProfile'