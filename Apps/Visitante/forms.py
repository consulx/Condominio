from django import forms
from Apps.Visitante.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = '__all__'
        labels = {
            'ci': 'CI.',
            'nombre': 'Nombres',
            'app': 'Apellido P.',
            'apm': 'Apellido M.',
            'tmp_estadia': 'Timepo Estadia',
            'mod_ing': 'Entro /en',
            'id_propietario': 'Visita A'
        }

        widgets = {
            'ci': forms.NumberInput(attrs={'class':'form-control col-5 col-sm-5 col-md-5', 'id':'ci'}),
            'nombre': forms.TextInput(attrs={'class':'form-control col-12 col-md-8', 'id':'nombre'}),
            'app': forms.TextInput(attrs={'class':'form-control col-12 col-md-8', 'id':'app'}),
            'apm': forms.TextInput(attrs={'class':'form-control col-12 col-md-8', 'id':'apm'}),
            'django.conf.locale.id': forms.TextInput(attrs={'class': 'form-control col-12 col-md-8', 'id': 'id_propietario'}),
            'tmp_estadia': forms.TimeInput(attrs={'class':'form-control col-5 col-sm-5 col-md-5', 'id':'tmp_estadia'}),
            'mod_ing': forms.Select(attrs={'class': 'form-control col-12 col-md-8', 'id': 'mod_ing'}),
        }