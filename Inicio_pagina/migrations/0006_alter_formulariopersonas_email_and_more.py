# Generated by Django 5.0.6 on 2024-05-25 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio_pagina', '0005_formulariopersonas_opciones_interes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulariopersonas',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='formulariopersonas',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formulariopersonas',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='formulariopersonas',
            name='opciones_interes',
            field=models.CharField(choices=[('Programacion', 'Programación'), ('Gestion_proyectos', 'Gestión de Proyectos'), ('Soporte_tecnico', 'Soporte técnico'), ('Testing', 'Testing'), ('Arquitecto_soluciones', 'Arquitecto de soluciones'), ('DBA', 'DBA'), ('Scrum_master', 'Scrum master'), ('Otro', 'Otro')], max_length=100),
        ),
        migrations.AlterField(
            model_name='formulariopersonas',
            name='profesion',
            field=models.CharField(max_length=100),
        ),
    ]