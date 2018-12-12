from django.db import models

# Create your models here.

CANCHAS = 'CAN'
PISCINAS = 'PIS'
CHURRASQUERAS = 'CHU'
GYM = 'GYM'

AREAS = (
    (CANCHAS, 'Cancha'),
    (PISCINAS, 'Piscina'),
    (CHURRASQUERAS, 'Churrasquera'),
    (GYM, 'Gym')
)


HABILITADO = 'H'
DESHABILITADO = 'D'
MANTENIMIENTO = 'M'

ESTADO = (
    (HABILITADO, 'Habilitado'),
    (DESHABILITADO, 'Deshabilitado'),
    (MANTENIMIENTO, 'Mantenimiento')
)

class AreaComun(models.Model):
    categoria = models.CharField(max_length=3, choices=AREAS)
    nombre = models.CharField(max_length=30, null=False)
    sector = models.CharField(max_length=30, null=False)
    imagen = models.FileField(null=False, upload_to='area_comun')
    descripcion = models.TextField(null=True, blank=True)
    disp_desde = models.TimeField()
    dip_hasta = models.TimeField()
    tmp_maximo = models.TimeField()
    estado = models.CharField(max_length=1, choices=ESTADO)
    created_at = models.DateTimeField(auto_now_add=True)  # Optiene la fecha de registro automaticamente
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.nombre)

