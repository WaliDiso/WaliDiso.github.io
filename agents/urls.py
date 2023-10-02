# books/urls.py
from django.urls import path
from .views import DestinationsListView, DestinationDetailView, SearchResultsListView

urlpatterns = [
    path("", DestinationsListView.as_view(), name="destination_list"),
    path("<uuid:pk>/", DestinationDetailView.as_view(), name="destination_detail"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
