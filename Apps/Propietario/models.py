from django.db import models

# Create your models here.

class Propietario(models.Model):
    nombre = models.CharField(max_length=30)
    app = models.CharField(max_length=30)
    apm = models.CharField(max_length=30)
    ci = models.CharField(max_length=12)
    nro_casa = models.CharField(max_length=10)

    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.app)
