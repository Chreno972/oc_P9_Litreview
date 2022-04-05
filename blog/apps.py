"""apps module for blog app."""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """_summary_

    Args:
        AppConfig (_type_): _description_
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
