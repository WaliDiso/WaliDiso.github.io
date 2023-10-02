from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone_number",
        "address",
        "origin",
        "destination",
        "departure_date",
        "message",
        "cover",
    )
