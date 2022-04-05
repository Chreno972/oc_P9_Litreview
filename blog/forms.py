"""forms module"""
from django import forms
from authentication.models import User
from . import models


class TicketForm(forms.ModelForm):
    """TicketForm class"""
    title = forms.CharField(
        max_length=20,
        label="",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Titre du ticket"}
        ),
    )
    description = forms.CharField(
        max_length=20,
        required=True,
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Description du ticket"
            }
        ),
    )

    class Meta:
        """Meta class"""
        model = models.Ticket
        fields = ["title", "description", "image"]


class CriticResponseForm(forms.ModelForm):
    """CriticResponseForm class"""
    headline = forms.CharField(
        max_length=60,
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Titre de la critique"
            }
        ),
    )
    body = forms.CharField(
        max_length=8192,
        required=True,
        label="",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "la critique"}
        ),
    )

    class Meta:
        """Meta class"""
        model = models.Critique
        fields = ["headline", "body", "rating"]


class FollowForm(forms.ModelForm):
    """FollowForm class"""
    class Meta:
        """Meta class"""
        model = User
        fields = ["follows"]
