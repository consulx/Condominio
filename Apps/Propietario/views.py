from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .models import Propietario
from Apps.Propietario.forms import PropietarioForm


class ListarPropietario(ListView):
    model = Propietario
    template_name = 'propietario/listar_propietario.html'
    context_object_name = 'propietario'
    paginate_by = 10

class RegistrarPropietario(CreateView):
    model = Propietario
    # fields = '__all__'
    form_class = PropietarioForm
    template_name = 'propietario/registrar_propietario.html'
    success_url = reverse_lazy('propietario:listar_propietario')

class EditarPropietario(UpdateView):
    model = Propietario
    form_class = PropietarioForm
    context_object_name = 'propietario'
    template_name = 'propietario/registrar_propietario.html'
    success_url = reverse_lazy('propietario:listar_propietario')

class EliminarPropietario(DeleteView):
    model = Propietario
    template_name = 'propietario/eliminar_propietario.html'
    success_url = reverse_lazy('propietario:listar_propietario')

class DetallePropietario(DetailView):
    model = Propietario
    context_object_name = 'propietario'
    template_name = 'propietario/detalle_propietario.html'



class BuscarPropietario(ListView):
    model = Propietario
    template_name = 'visitante/registrar_visita.html'
    context_object_name = 'propietario'

class BusquedaAjax(TemplateView):
    def get(self, request, *args, **kwargs):
        buscarPor = request.GET['id']
        buscar = request.GET['buscar']
        if buscarPor == "ci":
            propietario = Propietario.objects.filter(ci__contains=buscar)
        if buscarPor == "nombre":
            propietario = Propietario.objects.filter(nombre__contains=buscar)
        if buscarPor == "app":
            propietario = Propietario.objects.filter(app__contains=buscar)
        if buscarPor == "apm":
            propietario = Propietario.objects.filter(apm__contains=buscar)

        data = serializers.serialize('json', propietario,
                fields=('nombre', 'app', 'apm', 'ci', 'nro_casa'))
        return HttpResponse(data, content_type='application/json')