from django.urls import path
from django.contrib.auth.decorators import login_required
from Apps.usuario.views import RegistrarUsuario, ListarUsuario,\
    EditarUsuario, EliminarUsuario, DetalleUsuario

app_name = "usuario"

urlpatterns = [
    path('listar/', login_required(ListarUsuario.as_view()), name='listar_usuario'),
    path('detalle/<pk>/', login_required(DetalleUsuario.as_view()), name='detalle_usuario'),
    path('registrar/', login_required(RegistrarUsuario.as_view()), name='registrar_usuario'),
    path('editar/<pk>/', login_required(EditarUsuario.as_view()), name='editar_usuario'),
    path('eliminar/<pk>/', login_required(EliminarUsuario.as_view()), name='eliminar_usuario'),
]