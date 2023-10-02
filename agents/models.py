# agents/models.py
import uuid
from django.contrib.auth import get_user_model  # new
from django.db import models
from django.urls import reverse


class Destination(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover = models.ImageField(upload_to="covers/", blank=True)  # new
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [  # new
            models.Index(fields=["id"], name="id_index"),
        ]
        permissions = [
            ("special_status", "Can read all of the destinations"),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("destination_detail", args=[str(self.id)])


class Review(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
