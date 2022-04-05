"""urls.py module"""
from django.urls import path
from . import views

urlpatterns = [
    path("user_profile/<int:user_id>/", views.see_user, name="user_profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("home/", views.home, name="home"),
    path("posts/", views.posts, name="posts"),
    path("ticket_upload/", views.ticket_upload, name="ticket_upload"),
    path("abonnements/", views.abonnements, name="abonnements"),
    path(
        "critique_response/<int:cru_id>",
        views.critic_response_upload,
        name="critique_response",
    ),
    path(
        "standalone_critic/",
        views.standalone_critic,
        name="standalone_critic",
        ),
    path(
        "edit_ticket/<int:ticket_id>",
        views.edit_ticket,
        name="edit_ticket",
        ),
    path(
        "edit_critic/<int:critique_id>",
        views.edit_critic,
        name="edit_critic"
        ),
    path(
        "delete_ticket/<int:user_id>",
        views.delete_ticket,
        name="delete_ticket",
        ),
    path(
        "delete_critic/<int:user_id>",
        views.delete_critic,
        name="delete_critic",
        ),
]
