"""models module"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User model"""

    profile_photo = models.ImageField(
        upload_to="profile_photos/",
        default="profile_photos/default.png",
        blank=True,
        null=True,
    )
    follows = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False
    )

    def __str__(self):  # pylint: disable=invalid-str-returned
        return self.username
