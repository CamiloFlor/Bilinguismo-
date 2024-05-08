from usuarios.models import TipoSolicitud, Detallesolicitud                                 # Importing necessary modules and models
from django import forms
from usuarios.models import UserProfile
class UserProfileForm(forms.ModelForm):                                                     # Creating a form for the UserProfile model  
    class Meta:
        model = UserProfile
        fields = ['id_userprofile', 'nombre']  

class TipoSolicitudForm(forms.ModelForm):                                                    # Form for TipoSolicitud model
    class Meta:
        model = TipoSolicitud
        fields = ['id_tiposolicitud', 'nombre']                                              # Includes all fields of the model that you want in the form
        label='Tipos de Solicitud',
        
class DetalleSolicitudForm(forms.ModelForm):                                                # Form for Detallesolicitud model
    class Meta:
        model = Detallesolicitud
        exclude = ['id_categoria', 'id_ficha', 'id_programaformacion','id_municipio', 'id_modalidad', 'id_jornada'] 
        widgets = {
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
