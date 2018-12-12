from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from Apps.AreaComun.models import AreaComun
from Apps.Reserva.models import Reserva
from Apps.Reserva.forms import ReservaForm, DetalleReservaForm


class ListarReserva(ListView):
    model = Reserva
    template_name = 'reserva/listar_reserva.html'
    context_object_name = 'reserva'
    paginate_by = 10

# class RegistrarReserva(CreateView):
#     model = Reserva
#     # fields = '__all__'
#     form_class = ReservaForm
#     template_name = 'reserva/registrar_reserva.html'
#     success_url = reverse_lazy('reserva:listar_reserva')

class RegistrarReserva(CreateView):
    model = Reserva
    # fields = '__all__'
    template_name = 'reserva/registrar_reserva.html'
    form_class = ReservaForm
    second_form_class = DetalleReservaForm
    success_url = reverse_lazy('reserva:listar_reserva')

    def get_context_data(self, **kwargs):
        context = super(RegistrarReserva, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
            return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            reserva = form.save(commit=False)
            reserva.detallereserva_set = form2.save()
            reserva.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class EditarReserva(UpdateView):
    model = Reserva
    form_class = ReservaForm
    context_object_name = 'reserva'
    template_name = 'reserva/editar_reserva.html'
    success_url = reverse_lazy('reserva:listar_reserva')

class EliminarReserva(DeleteView):
    model = Reserva
    template_name = 'reserva/eliminar_reserva.html'
    success_url = reverse_lazy('reserva:listar_reserva')

class DetalleReserva(DetailView):
    model = Reserva
    context_object_name = 'reserva'
    template_name = 'reserva/detalle_reserva.html'

class BuscarArea(ListView):
    model = AreaComun
    template_name = 'reserva/registrar_reserva.html'
    context_object_name = 'area'

class BusquedaAjax(TemplateView):
    def get(self, request, *args, **kwargs):
        buscarPor = request.GET['id']
        buscar = request.GET['buscar']
        if buscarPor == "sector":
            areaComun = AreaComun.objects.filter(sector__icontains=buscar)
        if buscarPor == "area_comun":
            areaComun = AreaComun.objects.filter(nombre__icontains=buscar)
        if buscarPor == "estado":
            areaComun = AreaComun.objects.filter(estado__icontains=buscar)

        data = serializers.serialize('json', areaComun,
                fields=('pk', 'nombre', 'sector', 'tmp_maximo', 'estado'))
        return HttpResponse(data, content_type='application/json')