"""models module"""
from django.db import models
from django.conf import settings
from PIL import Image
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):
    """Ticket model"""
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank=True)
    image = models.ImageField(null=True, blank=True, verbose_name="Image")
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    time_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (310, 500)

    def resize_image(self):
        """_summary_: Resize image to fit in the ticket model
        """
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image

    class Meta:
        """Meta class"""
        ordering = ["-time_created"]

    # def __str__(self):
    #     return self.title


class Critique(models.Model):
    """Critique model"""
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        # validates that rating must be between 0 and 5
    )
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticket.title
