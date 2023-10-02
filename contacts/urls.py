# urls.py
from django.urls import path
from .views import (
    ContactView,
    contact_success,
    SuperuserOnlyListView,
    TouristDetailView,
)

urlpatterns = [
    path("", SuperuserOnlyListView.as_view(), name="tourists_list"),
    path("<uuid:pk>/", TouristDetailView.as_view(), name="tourist_detail"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("contact/success/", contact_success, name="contact_success"),
]
