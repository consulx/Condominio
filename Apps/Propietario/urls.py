from django.urls import path, include
from django.contrib.auth.decorators import login_required
from Apps.Propietario.views import RegistrarPropietario, ListarPropietario,\
    BusquedaAjax, EditarPropietario, EliminarPropietario, DetallePropietario

app_name = 'propietario'

urlpatterns = [
    path('listar/', login_required(ListarPropietario.as_view()), name="listar_propietario"),
    path('detalle/<pk>/', login_required(DetallePropietario.as_view()), name="detalle_propietario"),
    path('registrar/', login_required(RegistrarPropietario.as_view()), name="registrar_propietario"),
    path('editar/<pk>/', login_required(EditarPropietario.as_view()), name="editar_propietario"),
    path('eliminar/<pk>/', login_required(EliminarPropietario.as_view()), name="eliminar_propietario"),
    path('busquedaAjax/', login_required(BusquedaAjax.as_view()), name="busqueda_ajax"),
]