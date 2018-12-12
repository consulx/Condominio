from django.db import models

# Create your models here.
from Apps.AreaComun.models import AreaComun
from Apps.Propietario.models import Propietario


class Reserva(models.Model):
    fecha = models.DateField(null=False)
    id_propietario = models.ForeignKey(Propietario, null=False, blank=False, on_delete=models.CASCADE)
    area_social = models.ManyToManyField(AreaComun, through='DetalleReserva', related_name='detalle_reserva')
    created_at = models.DateTimeField(auto_now_add=True)  # Optiene la fecha de registro automaticamente
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.fecha)

class DetalleReserva(models.Model):
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    id_area_comun = models.ForeignKey(AreaComun, on_delete=models.CASCADE)
    hora = models.TimeField(null=False)
    tmp_uso = models.TimeField(null=False)