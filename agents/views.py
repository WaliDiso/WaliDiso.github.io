# books/views.py
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView

from .models import Destination


class DestinationsListView(LoginRequiredMixin, ListView):
    model = Destination
    context_object_name = "destination_list"  # new
    template_name = "agents/destination_list.html"
    login_url = "account_login"  # new


class DestinationDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Destination
    context_object_name = "trip"
    template_name = "agents/destination_detail.html"
    login_url = "account_login"  # new
    permission_required = "agents.special_status"
    queryset = Destination.objects.all().prefetch_related(
        "reviews__author",
    )  # new


class SearchResultsListView(ListView):
    model = Destination
    context_object_name = "destination_list"
    template_name = "agents/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Destination.objects.filter(
            Q(name__icontains=query) | Q(location__icontains=query)
        )
