
from django.core import validators
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuarios.models import UserProfile, Rol, TipoSolicitud, Detallesolicitud, Tipodocumento, Municipios

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
    # Define campos adicionales para el formulario de registro.
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        # Utiliza el modelo User de Django y define los campos a mostrar en el formulario.
        model = User
        fields = ['username',  'first_name', 'last_name', 'email', 'password1', 'password2']
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
            # Define el estilo del campo en el formulario.
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
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

# Define un formulario para el rol del usuario.
class RolForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        roles = kwargs.pop('roles', None)
        super(RolForm, self).__init__(*args, **kwargs)
        self.fields['id_rol'].label = 'Rol'
    class Meta:
        model = UserProfile
        fields = ['id_rol']
# Define un formulario para el tipo de documento del usuario.
class DocForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        doc = kwargs.pop('tipodoc', None)
        super(DocForm, self).__init__(*args, **kwargs)
        self.fields['id_doc'].label = 'Tipodocumento'
    class Meta:
        model = UserProfile
        fields = ['id_doc']
# Define un formulario para el tipo de solicitud.
class TipoSoliForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        tpsoli = kwargs.pop('tiposoli', None)
        super(TipoSoliForm, self).__init__(*args, **kwargs)
        self.fields['id_tiposolicitud'].label = 'TipoSolicitud'
    class Meta:
        model = Detallesolicitud
        fields = ['id_tiposolicitud']


