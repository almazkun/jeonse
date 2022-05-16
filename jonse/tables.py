import django_tables2 as tables

from jonse.models import Listing


class ListingTable(tables.Table):
    class Meta:
        model = Listing
        template_name = "tables/listing_table.html"
        attrs = {"class": "table table-responsive"}
