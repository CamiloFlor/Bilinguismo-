from usuarios.models import  TipoSolicitud, Detallesolicitud
from django import forms
from usuarios.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['id_userprofile', 'nombre']  

class TipoSolicitudForm(forms.ModelForm):
    class Meta:
        model = TipoSolicitud
        fields = ['id_tiposolicitud', 'nombre']  # Incluye todos los campos del modelo que deseas en el formulario
        label='Tipos de Solicitud',
        
class DetalleSolicitudForm(forms.ModelForm):
    class Meta:
        model = Detallesolicitud
        exclude = ['id_categoria', 'id_ficha', 'id_programaformacion','id_municipio', 'id_modalidad', 'id_jornada'] 
        widgets = {
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


