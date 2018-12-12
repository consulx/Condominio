from django.urls import path, include
from django.contrib.auth.decorators import login_required
from Apps.Reserva.views import RegistrarReserva, ListarReserva,\
    EditarReserva, EliminarReserva, DetalleReserva, BusquedaAjax

app_name = 'reserva'

urlpatterns = [
    path('listar/', login_required(ListarReserva.as_view()), name="listar_reserva"),
    path('detalle/<pk>/', login_required(DetalleReserva.as_view()), name="detalle_reserva"),
    path('registrar/', login_required(RegistrarReserva.as_view()), name="registrar_reserva"),
    path('editar/<pk>/', login_required(EditarReserva.as_view()), name="editar_reserva"),
    path('eliminar/<pk>/', login_required(EliminarReserva.as_view()), name="eliminar_reserva"),
    path('busquedaAjax/', login_required(BusquedaAjax.as_view()), name="busqueda_ajax"),
]