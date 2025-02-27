from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
     
     # import our userssignal
    def ready(self):
        import users.signals 