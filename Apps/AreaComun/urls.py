from django.urls import path, include
from django.contrib.auth.decorators import login_required
from Apps.AreaComun.views import RegistrarAreaComun, ListarAreaComun,\
    EditarAreaComun, EliminarAreaComun, DetalleAreaComun

app_name = 'areaComun'

urlpatterns = [
    path('listar/', login_required(ListarAreaComun.as_view()), name="listar_areaComun"),
    path('detalle/<pk>/', login_required(DetalleAreaComun.as_view()), name="detalle_areaComun"),
    path('registrar/', login_required(RegistrarAreaComun.as_view()), name="registrar_areaComun"),
    path('editar/<pk>/', login_required(EditarAreaComun.as_view()), name="editar_areaComun"),
    path('eliminar/<pk>/', login_required(EliminarAreaComun.as_view()), name="eliminar_areaComun"),
]