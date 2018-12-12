from django import forms
from Apps.Reserva.models import Reserva, DetalleReserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        labels = {
            'fecha': 'Fecha',
            'id_propietario': 'Propietario',
        }

        widgets = {
            'hora': forms.TextInput(attrs={'class':'form-control col-12 col-md-8', 'id':'hora'}),
            'tmp_uso': forms.TextInput(attrs={'class':'form-control col-12 col-md-8', 'id':'tmp_uso'}),
            'django.conf.locale.id': forms.TextInput(attrs={'class': 'form-control col-12 col-md-8', 'id': 'id_propietario'}),
        }

class DetalleReservaForm(forms.ModelForm):
    class Meta:
        model = DetalleReserva
        fields = '__all__'
        labels = {
            'id_reserva': 'ID Reserva',
            'id_area_comun': 'ID Area Comun',
            'hora': 'Hora',
            'tmp_uso': 'Timepo Uso',
        }

        widgets = {
            'id_reserva': forms.TextInput(attrs={'class': 'form-control col-12 col-md-8', 'id': 'id_reserva'}),
            'id_area_comun': forms.TextInput(attrs={'class': 'form-control col-12 col-md-8', 'id': 'id_area_comun'}),
            'hora': forms.TextInput(attrs={'class':'form-control col-12 col-md-8', 'id':'hora'}),
            'tmp_uso': forms.TextInput(attrs={'class':'form-control col-12 col-md-8', 'id':'tmp_uso'}),
        }