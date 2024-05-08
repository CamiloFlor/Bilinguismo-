from django.apps import AppConfig                                               # Importing AppConfig from django.apps module
class CoordinacionConfig(AppConfig):                                            # Configuration for the 'coordinacion' app

    default_auto_field = 'django.db.models.BigAutoField'                        # Configuring the default auto field for models
 
    name = 'coordinacion'                                                      # Setting the name of the app
