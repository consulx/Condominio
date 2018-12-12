from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Visitante
from Apps.Visitante.forms import VisitanteForm


class ListarVisitante(ListView):
    model = Visitante
    template_name = 'visitante/listar_visita.html'
    context_object_name = 'visitante'
    paginate_by = 10

class RegistrarVisitante(CreateView):
    model = Visitante
    # fields = '__all__'
    form_class = VisitanteForm
    template_name = 'visitante/registrar_visita.html'
    success_url = reverse_lazy('visitante:listar_visitante')

class EditarVisitante(UpdateView):
    model = Visitante
    form_class = VisitanteForm
    context_object_name = 'visitante'
    template_name = 'visitante/editar_visita.html'
    success_url = reverse_lazy('visitante:listar_visitante')

class EliminarVisitante(DeleteView):
    model = Visitante
    template_name = 'visitante/eliminar_visita.html'
    success_url = reverse_lazy('visitante:listar_visitante')

class DetalleVisitante(DetailView):
    model = Visitante
    context_object_name = 'visitante'
    template_name = 'visitante/detalle_visita.html'