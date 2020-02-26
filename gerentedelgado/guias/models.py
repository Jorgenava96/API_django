from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=80)
    apellido_pate = models.CharField(max_length=20)
    apellido_mater = models.CharField(max_length=20)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
