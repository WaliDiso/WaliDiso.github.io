# views.py
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactForm

from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import ContactMessage


class SuperuserOnlyListView(UserPassesTestMixin, ListView):
    model = ContactMessage
    context_object_name = "tourists"
    template_name = "tourists_list.html"

    def test_func(self):
        # Check if the user is a superuser
        return self.request.user.is_superuser

    def handle_no_permission(self):
        # Customize this behavior as needed
        raise Http404("You don't have permission to access this page.")

    def get_queryset(self):
        # Get the list of objects to display
        return ContactMessage.objects.all()


class TouristDetailView(DetailView):
    model = ContactMessage
    context_object_name = "tourists"
    template_name = "tourist_detail.html"


class ContactView(FormView):
    template_name = "contact_form.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact_success")

    def form_valid(self, form):
        # Save the form data to the database
        message = ContactMessage(
            name=form.cleaned_data["name"],
            email=form.cleaned_data["email"],
            message=form.cleaned_data["message"],
            departure_date=form.cleaned_data["departure_date"],
            phone_number=form.cleaned_data["phone_number"],
            origin=form.cleaned_data["origin"],
            destination=form.cleaned_data["destination"],
            cover=form.cleaned_data["cover"],
        )

        message.save()
        # You can add additional logic here, like sending an email
        return super().form_valid(form)


def contact_success(request):
    return HttpResponse("Contact form submitted successfully.")
