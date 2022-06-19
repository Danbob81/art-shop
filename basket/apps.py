from django.apps import AppConfig


class BasketConfig(AppConfig):
    """ Config for basket app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basket'
