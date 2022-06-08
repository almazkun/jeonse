import django_filters

from jeonse.models import Listing


class ListingFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="universal_search", label="")

    class Meta:
        model = Listing
        fields = ["query"]

    def universal_search(self, queryset, name, value):
        return Listing.objects.filter(name__icontains=value)
