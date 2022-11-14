from django.db import models
from datetime import date

# Create your models here.
class Repaso(models.Model):

    clase = models.IntegerField()
    tema_a_repasar = models.CharField(max_length=40)
    fecha_repaso = models.DateField(default=date.today())