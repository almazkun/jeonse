from django.urls import path

from jonse.views import HomeView, ListingCreateView, MyListingView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("my/", MyListingView.as_view(), name="my_listings"),
    path("my/listing/create/", ListingCreateView.as_view(), name="listing_create"),
]
