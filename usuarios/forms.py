from django.core import validators
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuarios.models import UserProfile, Rol, TipoSolicitud, Detallesolicitud, Tipodocumento


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ['username',  'first_name', 'last_name','email', 'password1', 'password2']
        labels = {
            'username': 'Numero de Identificacion',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electronico',
            'rol': 'Rol',



        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
           
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            

             'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class RolForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        roles = kwargs.pop('roles', None)
        super(RolForm, self).__init__(*args, **kwargs)
        self.fields['id_rol'].label = 'Rol'
    class Meta:
        model = UserProfile
        fields = ['id_rol']

class DocForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        doc = kwargs.pop('tipodoc', None)
        super(DocForm, self).__init__(*args, **kwargs)
        self.fields['id_doc'].label = 'Tipodocumento'
    class Meta:
        model = UserProfile
        fields = ['id_doc']
class TipoSoliForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        tpsoli = kwargs.pop('tiposoli', None)
        super(TipoSoliForm, self).__init__(*args, **kwargs)
        self.fields['id_tiposolicitud'].label = 'TipoSolicitud'
    class Meta:
        model = Detallesolicitud
        fields = ['id_tiposolicitud']
