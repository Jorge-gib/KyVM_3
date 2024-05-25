from django.db import models

class Formulario(models.Model):
    OPCIONES_CONTACTO = [
        ('telefono', 'Comunicarse por teléfono'),
        ('email', 'Comunicarse por email'),
    ]

    nombre = models.CharField(max_length=50)
    empresa = models.CharField(max_length=100, blank=True, null=True, default=None)
    telefono = models.IntegerField()
    email = models.CharField(max_length=150)
    motivo_contacto = models.CharField(max_length=400)
    forma_contacto = models.CharField(max_length=20, choices=OPCIONES_CONTACTO)

    def __str__(self):
        return self.empresa

class FormularioPersonas(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)
    opciones_interes = models.CharField(max_length=100, choices=[
        ('Programacion', 'Programación'),
        ('Gestion_proyectos', 'Gestión de Proyectos'),
        ('Soporte_tecnico', 'Soporte técnico'),
        ('Testing', 'Testing'),
        ('Arquitecto_soluciones', 'Arquitecto de soluciones'),
        ('DBA', 'DBA'),
        ('Scrum_master', 'Scrum master'),
        ('Otro', 'Otro')
    ])
    cv = models.FileField(upload_to='cv/')
    linkedin_url = models.URLField(blank=True, null=True)