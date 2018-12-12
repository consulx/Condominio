from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .models import AreaComun
from Apps.AreaComun.forms import AreaComunForm


class ListarAreaComun(ListView):
    model = AreaComun
    template_name = 'areaComun/listar_areaComun.html'
    context_object_name = 'areaComun'
    paginate_by = 10

class RegistrarAreaComun(CreateView):
    model = AreaComun
    # fields = '__all__'
    form_class = AreaComunForm
    template_name = 'areaComun/registrar_areaComun.html'
    success_url = reverse_lazy('areaComun:listar_areaComun')

class EditarAreaComun(UpdateView):
    model = AreaComun
    form_class = AreaComunForm
    context_object_name = 'areaComun'
    template_name = 'areaComun/editar_areaComun.html'
    success_url = reverse_lazy('areaComun:listar_areaComun')

class EliminarAreaComun(DeleteView):
    model = AreaComun
    template_name = 'areaComun/eliminar_areaComun.html'
    success_url = reverse_lazy('areaComun:listar_areaComun')

class DetalleAreaComun(DetailView):
    model = AreaComun
    context_object_name = 'areaComun'
    template_name = 'areaComun/detalle_areaComun.html'