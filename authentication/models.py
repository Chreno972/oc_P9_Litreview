"""models module"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User model"""
    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = (
        (CREATOR, "Créateur"),
        (SUBSCRIBER, "Abonné"),
    )

    profile_photo = models.ImageField(
        upload_to="profile_photos/",
        default="profile_photos/default.png",
        blank=True,
        null=True,
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=SUBSCRIBER,
        )
    follows = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False
    )

    def __str__(self):  # pylint: disable=invalid-str-returned
        return self.username
