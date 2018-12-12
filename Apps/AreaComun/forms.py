from django import forms
from Apps.AreaComun.models import AreaComun

class AreaComunForm(forms.ModelForm):
    class Meta:
        model = AreaComun
        fields = '__all__'
        labels = {
            'categoria': 'Categoria',
            'nombre': 'Nombre del Area',
            'sector': 'Sector',
            'imagen': 'Imagen',
            'descripcion': 'Descipcion',
            'disp_desde': 'Disponible desde',
            'dip_hasta': 'Disponible hasta',
            'tmp_maximo': 'Tiempo Maximo de Uso',
            'estado': 'Estado'
        }

        widgets = {
            'categoria': forms.Select(attrs={'class': 'custom-select col-12 col-md-8', 'id': 'categoria'}),
            'nombre': forms.TextInput(attrs={'class':'form-control col-12 col-md-8', 'id':'nombre'}),
            'sector': forms.TextInput(attrs={'class':'form-control col-12 col-md-8', 'id':'sector'}),
            'imagen': forms.FileInput(attrs={'class':'form-control col-5 col-sm-5 col-md-5', 'id':'imagen'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control col-12 col-md-8', 'id':'descripcion', 'rows':"3"}),
            'disp_desde': forms.TimeInput(attrs={'class':'form-control col-5 col-sm-5 col-md-5', 'id':'dis_desde'}),
            'dip_hasta': forms.TimeInput(attrs={'class':'form-control col-5 col-sm-5 col-md-5', 'id':'dis_hasta'}),
            'tmp_maximo': forms.TimeInput(attrs={'class': 'form-control col-5 col-sm-5 col-md-5', 'id': 'tmp_maximo'}),
            'estado': forms.Select(attrs={'class': 'form-control col-12 col-md-8', 'id': 'estado'}),
        }