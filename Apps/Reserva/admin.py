from django.contrib import admin

# Register your models here.
from Apps.Reserva.models import Reserva, DetalleReserva


class DetalleReservaInline(admin.TabularInline):
    model = DetalleReserva

class ReservaAdmin(admin.ModelAdmin):
    inlines = (DetalleReservaInline,)


admin.site.register(Reserva, ReservaAdmin)
