from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from jonse.filters import ListingFilter
from jonse.models import Listing
from jonse.tables import ListingTable


# Create your views here.
class HomeView(SingleTableMixin, FilterView):
    table_class = ListingTable
    queryset = Listing.objects.for_home()
    paginate_by = 15
    filterset_class = ListingFilter

    def get_template_names(self):

        if self.request.htmx:
            template_name = "home_partial.html"
        else:
            template_name = "home.html"

        return template_name
