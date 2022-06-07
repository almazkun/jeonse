from django.urls import path

from jonse.views import (
    HomeView,
    ListingCreateView,
    ListingDeleteView,
    ListingDetailView,
    MyListingView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("my/", MyListingView.as_view(), name="my_listings"),
    path("my/listing/create/", ListingCreateView.as_view(), name="listing_create"),
    path("my/listing/<int:pk>/", ListingDetailView.as_view(), name="listing_detail"),
    path(
        "my/listing/<int:pk>/delete/",
        ListingDeleteView.as_view(),
        name="listing_delete",
    ),
]
