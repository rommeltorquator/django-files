from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

    # additional configuration for signals
    def ready(self):
        import users.signals