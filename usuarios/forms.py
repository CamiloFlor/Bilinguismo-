from django.core import validators
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuarios.models import UserProfile, Rol, TipoSolicitud, Detallesolicitud, Tipodocumento, Municipio

class DetalleSolicitudForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DetalleSolicitudForm, self).__init__(*args, **kwargs)
        self.fields['id_municipio'].queryset = Municipio.objects.all().values_list('nombre', flat=True)
        self.fields['id_tiposolicitud'].queryset = TipoSolicitud.objects.all().values_list('nombre', flat=True)
    class Meta:
        model = Detallesolicitud
        exclude = ['id_categoria', 'id_ficha', 'fecha_inicio','fecha_fin', 'id_modalidad', 'imagen', 'url'] 
        labels = {
            'id_municipio': 'DE DONDE ES SU SOLICITUD ?'
        }
        widgets = {
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username': 'Numero de Identificacion',
        }

class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        roles = kwargs.pop('roles', None)
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['id_rol'].label = 'Rol'
    class Meta:
        model = UserProfile
        fields = ['id_rol']

class TipoDocumentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TipoDocumentoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = 'Nombre'

    class Meta:
        model = Tipodocumento
        fields = ['nombre']