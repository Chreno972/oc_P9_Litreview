"""admin module"""
from django.contrib import admin
from blog.models import Ticket, Critique
from authentication.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin"""
    list_display = ("id", "username", "email", "role", "is_active")
    list_filter = ("role", "is_active")


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    """Ticket admin"""
    list_display = ("id", "title", "description", "user", "time_created")


@admin.register(Critique)
class CritiqueAdmin(admin.ModelAdmin):
    """Critique admin"""
    list_display = ("headline", "body", "user", "time_created")
