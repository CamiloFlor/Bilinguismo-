from django.apps import AppConfig                                        # Importa la clase AppConfig de Django.
class UsuariosConfig(AppConfig):                                         # Define una configuración para la aplicación 'usuarios'.
    default_auto_field = 'django.db.models.BigAutoField'                 # Define el campo de auto-generación predeterminado para modelos de la base de datos.
    name = 'usuarios'                                                    # Define el nombre de la aplicación.
