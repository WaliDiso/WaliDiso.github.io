# views.py
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactMessageForm
from .models import ContactPage
from django.views.generic import ListView, DetailView, TemplateView

from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import Http404


class SuperuserOnlyListView(UserPassesTestMixin, ListView):
    model = ContactPage
    context_object_name = "contacts"
    template_name = "contacts_list.html"

    def test_func(self):
        # Check if the user is a superuser
        return self.request.user.is_superuser

    def handle_no_permission(self):
        # Customize this behavior as needed
        raise Http404("You don't have permission to access this page.")

    def get_queryset(self):
        # Get the list of objects to display
        return ContactPage.objects.all()


class ContactPageView(FormView):
    template_name = "contact.html"
    form_class = ContactMessageForm
    success_url = reverse_lazy("contact_success")

    def form_valid(self, form):
        message = ContactPage(
            name=form.cleaned_data["name"],
            email=form.cleaned_data["email"],
            message=form.cleaned_data["message"],
        )

        message.save()
        return super().form_valid(form)


class ContactDetailView(DetailView):
    model = ContactPage
    context_object_name = "contacts"
    template_name = "contact_detail.html"


def contact_success(request):
    return HttpResponse("Contact form submitted successfully.")
