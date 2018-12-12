from django import forms
from Apps.Propietario.models import Propietario

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'
        labels = {
            'ci': 'CI.',
            'nombre': 'Nombres',
            'app': 'Apellido P.',
            'apm': 'Apellido M.',
            'nro_casa': 'Nro. Casa'
        }

        widgets = {
            'ci': forms.NumberInput(attrs={'class':'form-control col-5 col-sm-5 col-md-5', 'id':'ci'}),
            'nombre': forms.TextInput(attrs={'class':'form-control col-12 col-md-8', 'nombre':'nombre'}),
            'app': forms.TextInput(attrs={'class':'form-control col-12 col-md-8', 'app':'app'}),
            'apm': forms.TextInput(attrs={'class':'form-control col-12 col-md-8', 'apm':'apm'}),
            'nro_casa': forms.NumberInput(attrs={'class':'form-control col-5 col-sm-5 col-md-5', 'nro_casa':'nro_casa'}),
        }