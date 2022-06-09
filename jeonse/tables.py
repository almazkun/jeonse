import django_tables2 as tables
from django_tables2.utils import A

from jeonse.models import Listing


class ListingTable(tables.Table):
    class Meta:
        model = Listing
        template_name = "tables/listing_table.html"
        attrs = {"class": "table table-sm table-responsive table-hover"}
        empty_text = "There are no listings yet"
        fields = (
            "name",
            "jeonse_amount",
            "wolse_amount",
            "monthly_expense",
            "number_of_rooms",
            "number_of_bathrooms",
            "condition",
            "description",
        )


class MyListingTable(ListingTable):
    edit = tables.LinkColumn(
        "listing_detail", args=[A("pk")], orderable=False, empty_values=()
    )

    class Meta(ListingTable.Meta):
        pass

    def render_edit(self, value):
        return "edit"
