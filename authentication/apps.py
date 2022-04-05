"""apps module for authentication app."""
from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """_summary_

    Args:
        AppConfig (_type_): _description_
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
