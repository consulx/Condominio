from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields= [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels={
            'username': 'Usuario',
            'first_name': 'Nombre Usuario',
            'last_name': 'Apellido',
            'email': 'Email',
        }