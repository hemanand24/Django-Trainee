from django.apps import AppConfig


class Sig1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sig1'


    def ready(self):
        import sig1.signals