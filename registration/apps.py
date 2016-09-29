from django.apps import AppConfig


class RegistrationConfig(AppConfig):
    name = 'registration'
    
    def ready(self):
        # noinspection PyUnresolvedReferences
        from . import signals  # noqua
