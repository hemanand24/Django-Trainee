from django.apps import AppConfig


class Sig3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sig3'

    def ready(self):
        import sig3.signals
