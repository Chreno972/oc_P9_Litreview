"""urls module"""
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path(
        "",
        LoginView.as_view(
            template_name="authentication/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("signup/", views.signup_page, name="signup"),
    path("logout/", views.logout_page, name="logout"),
]
