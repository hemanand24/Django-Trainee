from django.apps import AppConfig


class Sig2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sig2'

    def ready(self):
        import sig2.signals
