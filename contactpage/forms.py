from django import forms
from .models import ContactPage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = [
            "name",
            "email",
            "message",
        ]
