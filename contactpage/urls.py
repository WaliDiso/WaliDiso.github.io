# urls.py
from django.urls import path
from .views import ContactPageView, SuperuserOnlyListView, ContactDetailView

urlpatterns = [
    path("", SuperuserOnlyListView.as_view(), name="contacts_list"),
    path("contactpage/", ContactPageView.as_view(), name="contactpage"),
    path("<int:pk>/", ContactDetailView.as_view(), name="contact_detail"),
]
