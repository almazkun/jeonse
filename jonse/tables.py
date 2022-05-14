import django_tables2 as tables

from jonse.models import Listing


class ListingTable(tables.Table):
    class Meta:
        model = Listing
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name", "jonse_amount", "wolse_amount", "monthly_rent", "kollibi")
