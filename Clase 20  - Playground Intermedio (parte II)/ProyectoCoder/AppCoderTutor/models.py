from django.db import models
from django.utils.timezone import now

# Create your models here.
class Curso(models.Model):

    # VARCHAR(100)
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    esta_activo = models.BooleanField(default=True)

class Repaso(models.Model):

    clase = models.IntegerField()
    tema_a_repasar = models.CharField(max_length=40)
    fecha_repaso = models.DateField(default=now())
