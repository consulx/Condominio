from django.db import models

# Create your models here.
from Apps.Propietario.models import Propietario

AUTOMOVIL = 'AUTO'
CAMINANDO = 'PIE'
BICICLETA = 'BICI'

INGRESO = (
    (AUTOMOVIL, 'Automovil'),
    (CAMINANDO, 'Caminando'),
    (BICICLETA, 'Bicicleta')
)

class Visitante(models.Model):
    ci = models.CharField(max_length=12, null=False)
    nombre = models.CharField(max_length=30, null=False)
    app = models.CharField(max_length=30, null=False)
    apm = models.CharField(max_length=30, null=False)
    tmp_estadia = models.TimeField()
    mod_ing = models.CharField(max_length=10, choices=INGRESO)
    id_propietario = models.ForeignKey(Propietario, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Optiene la fecha de registro automaticamente
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.app)