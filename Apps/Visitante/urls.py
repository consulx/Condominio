from django.urls import path, include
from django.contrib.auth.decorators import login_required
from Apps.Visitante.views import RegistrarVisitante, ListarVisitante,\
    EditarVisitante, EliminarVisitante, DetalleVisitante

app_name = 'visitante'

urlpatterns = [
    path('listar/', login_required(ListarVisitante.as_view()), name="listar_visitante"),
    path('detalle/<pk>/', login_required(DetalleVisitante.as_view()), name="detalle_visitante"),
    path('registrar/', login_required(RegistrarVisitante.as_view()), name="registrar_visitante"),
    path('editar/<pk>/', login_required(EditarVisitante.as_view()), name="editar_visitante"),
    path('eliminar/<pk>/', login_required(EliminarVisitante.as_view()), name="eliminar_visitante"),
]