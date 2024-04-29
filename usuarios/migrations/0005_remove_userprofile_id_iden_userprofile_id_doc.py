# Generated by Django 5.0.2 on 2024-04-21 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_rename_cod_poblado_poblacion_cod_poblacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='id_iden',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='id_doc',
            field=models.ForeignKey(blank=True, db_column='id_doc', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.tipodocumento'),
        ),
    ]