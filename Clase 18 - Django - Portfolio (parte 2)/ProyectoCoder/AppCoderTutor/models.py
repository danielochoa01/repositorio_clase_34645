from django.db import models

# Create your models here.
class Curso(models.Model):

    # VARCHAR(100)
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    esta_activo = models.BooleanField(default=True)
