# Generated by Django 5.0.2 on 2024-04-21 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_municipios_cod_dpto_poblados_cod_municipio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poblacion',
            fields=[
                ('cod_poblado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_poblacion', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'poblacion',
                'managed': True,
            },
        ),
    ]