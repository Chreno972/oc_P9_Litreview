"""forms module"""
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class EditProfileForm(UserChangeForm):
    """Edit profile form"""
    class Meta:
        """_summary_    : Meta class
        _description_ : Meta class
        _return_      : Meta class
        """
        model = User
        fields = ("username", "email", "profile_photo")


class LoginForm(forms.Form):
    """Login form"""
    username = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nom d'utilisateur"
            }
            ),
    )
    password = forms.CharField(
        max_length=63,
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Mot de passe"
                }
        ),
    )


class SignupForm(UserCreationForm):
    """Signup form"""
    username = forms.CharField(
        max_length=12,
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nom d'utilisateur"
            }
        ),
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        label="",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Adresse email"
            }
        ),
    )
    password1 = forms.CharField(
        max_length=30,
        required=True,
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Mot de passe"
            }
        ),
    )
    password2 = forms.CharField(
        max_length=30,
        required=True,
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirmer mot de passe"
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        """_summary_    : Meta class
        _description_ : Meta class
        _return_      : Meta class
        """
        model = get_user_model()
        fields = ("username", "email", "password1", "password2", "role")
