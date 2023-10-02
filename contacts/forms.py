# forms.py
from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            "name",
            "email",
            "phone_number",
            "address",
            "origin",
            "destination",
            "price",
            "departure_date",
            "message",
            "cover",
        ]

    phone_number = forms.DecimalField(required=False)
    price = forms.DecimalField(required=False)
    departure_date = forms.DateField(
        required=False, widget=forms.DateInput(attrs={"placeholder": "YYYY-MM-DD"})
    )
