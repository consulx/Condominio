from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from Apps.usuario.forms import RegistroUsuarioForm
# Create your views here.

class ListarUsuario(ListView):
    model = User
    template_name = 'usuario/listar_usuario.html'
    context_object_name = 'usuario'
    paginate_by = 10

class RegistrarUsuario(CreateView):
    model = User
    form_class = RegistroUsuarioForm
    template_name = 'usuario/registrar_usuario.html'
    success_url = reverse_lazy('usuario:listar_usuario')


class EditarUsuario(UpdateView):
    model = User
    form_class = RegistroUsuarioForm
    context_object_name = 'usuario'
    template_name = 'usuario/editar_usuario.html'
    success_url = reverse_lazy('usuario:listar_usuario')

class EliminarUsuario(DeleteView):
    model = User
    template_name = 'usuario/eliminar_usuario.html'
    success_url = reverse_lazy('usuario:listar_usuario')

class DetalleUsuario(DetailView):
    model = User
    context_object_name = 'usuario'
    template_name = 'usuario/detalle_usuario.html'