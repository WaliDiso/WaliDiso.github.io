# agents/admin.py
from django.contrib import admin
from .models import Destination, Review

class ReviewInline(admin.TabularInline):
    model = Review

class DestinationAdmin(admin.ModelAdmin):

    inlines = [
        ReviewInline,
        ]

    list_display = (
        "name",
        "location",
        "price",
    )

admin.site.register(Destination, DestinationAdmin)
