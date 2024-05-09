<<<<<<< HEAD
from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'
=======
from django.apps import AppConfig                                        # Importa la clase AppConfig de Django.
class UsuariosConfig(AppConfig):                                         # Define una configuración para la aplicación 'usuarios'.
    default_auto_field = 'django.db.models.BigAutoField'                 # Define el campo de auto-generación predeterminado para modelos de la base de datos.
    name = 'usuarios'                                                    # Define el nombre de la aplicación.
>>>>>>> 9dbd9c1b52866ecd1ff328aa990b020db312123f
