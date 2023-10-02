import uuid
from django.contrib.auth import get_user_model  # new
from django.db import models
from django.urls import reverse


class ContactMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255)
    origin = models.CharField(max_length=300)
    destination = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    departure_date = models.DateField(null=True, blank=True)
    message = models.TextField()
    cover = models.ImageField(upload_to="covers/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tourist_detail", args=[str(self.id)])
