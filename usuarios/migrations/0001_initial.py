# Generated by Django 5.0.2 on 2024-04-04 19:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id_calificacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=250, null=True)),
                ('id_userprofile', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'calificacion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'categoria',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id_competencia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'Competencia',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estadoxinstru',
            fields=[
                ('id_estadoxinstru', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_suspe', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'estadoxinstru',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'genero',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id_jornada', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'jornada',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mcer',
            fields=[
                ('id_mcer', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'mcer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id_modalidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'modalidad',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Nivelformacion',
            fields=[
                ('id_nivel_formacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'nivelformacion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Poblacion',
            fields=[
                ('id_poblacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'poblacion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'rol',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id_sector', models.AutoField(primary_key=True, serialize=False)),
                ('barrio', models.CharField(blank=True, db_column='Barrio', max_length=200, null=True)),
                ('comuna', models.CharField(blank=True, db_column='Comuna', max_length=200, null=True)),
                ('direccion', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'sector',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tipodocumento',
            fields=[
                ('id_doc', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'tipodocumento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoSolicitud',
            fields=[
                ('id_tiposolicitud', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'tiposolicitud',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tpestado',
            fields=[
                ('id_tpestado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'tpestado',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id_municipio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('id_poblacion', models.ForeignKey(blank=True, db_column='id_poblacion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.poblacion')),
                ('id_sector', models.ForeignKey(blank=True, db_column='id_sector', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.sector')),
            ],
            options={
                'db_table': 'municipio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Programaformacion',
            fields=[
                ('id_programaformacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('id_competencia', models.ForeignKey(blank=True, db_column='id_competencia', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.competencia')),
                ('id_jornada', models.ForeignKey(blank=True, db_column='id_jornada', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.jornada')),
                ('id_mcer', models.ForeignKey(blank=True, db_column='id_mcer', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.mcer')),
                ('id_modalidad', models.ForeignKey(blank=True, db_column='id_modalidad', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.modalidad')),
                ('id_nivel_formacion', models.ForeignKey(blank=True, db_column='id_nivel_formacion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.nivelformacion')),
            ],
            options={
                'db_table': 'programaformacion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id_ficha', models.AutoField(primary_key=True, serialize=False)),
                ('ficha', models.IntegerField(blank=True, null=True)),
                ('id_programaformacion', models.ForeignKey(blank=True, db_column='id_programaformacion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.programaformacion')),
            ],
            options={
                'db_table': 'ficha',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Detallesolicitud',
            fields=[
                ('id_detallesolicitud', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('archivo', models.TextField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('imagen', models.TextField(blank=True, db_column='Imagen', null=True)),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True)),
                ('id_categoria', models.ForeignKey(blank=True, db_column='id_categoria', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.categoria')),
                ('id_ficha', models.ForeignKey(blank=True, db_column='id_ficha', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.ficha')),
                ('id_jornada', models.ForeignKey(blank=True, db_column='id_jornada', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.jornada')),
                ('id_modalidad', models.ForeignKey(blank=True, db_column='id_modalidad', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.modalidad')),
                ('id_municipio', models.ForeignKey(blank=True, db_column='id_municipio', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.municipio')),
                ('id_programaformacion', models.ForeignKey(blank=True, db_column='id_programaformacion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.programaformacion')),
            ],
            options={
                'db_table': 'detallesolicitud',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Resultadosaprendizaje',
            fields=[
                ('id_resultado_aprendizaje', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=150, null=True)),
                ('id_competencia', models.ForeignKey(blank=True, db_column='id_competencia', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.competencia')),
            ],
            options={
                'db_table': 'resultadosaprendizaje',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id_userprofile', models.AutoField(primary_key=True, serialize=False)),
                ('numeroiden', models.IntegerField(blank=True, null=True, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('nombre2', models.CharField(blank=True, max_length=30, null=True)),
                ('apellido', models.CharField(blank=True, max_length=30, null=True)),
                ('apellido2', models.CharField(blank=True, max_length=30, null=True)),
                ('celular', models.CharField(blank=True, max_length=11, null=True)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
                ('correo1', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('id_estadoxinstru', models.ForeignKey(blank=True, db_column='id_estadoxinstru', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.estadoxinstru')),
                ('id_ficha', models.ForeignKey(blank=True, db_column='id_ficha', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.ficha')),
                ('id_genero', models.ForeignKey(blank=True, db_column='id_genero', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.genero')),
                ('id_iden', models.ForeignKey(blank=True, db_column='id_iden', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.tipodocumento')),
                ('id_municipio', models.ForeignKey(blank=True, db_column='id_municipio', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.municipio')),
                ('id_poblacion', models.ForeignKey(blank=True, db_column='id_poblacion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.poblacion')),
                ('id_rol', models.ForeignKey(blank=True, db_column='id_rol', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.rol')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserProfile',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('id_calificacion', models.ForeignKey(blank=True, db_column='id_calificacion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.calificacion')),
                ('id_tpestado', models.ForeignKey(blank=True, db_column='id_tpestado', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.tpestado')),
                ('id_userprofile', models.ForeignKey(blank=True, db_column='id_userprofile', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.userprofile')),
            ],
            options={
                'db_table': 'solicitud',
                'managed': True,
            },
        ),
    ]
