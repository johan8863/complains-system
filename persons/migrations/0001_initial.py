# Generated by Django 3.2 on 2021-09-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=250, verbose_name='Apellidos')),
                ('sex', models.CharField(choices=[('m', 'Masculino'), ('f', 'Femenino')], max_length=1, verbose_name='Sexo')),
                ('demmanded', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]
