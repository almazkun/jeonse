import django_tables2 as tables
from django_tables2.utils import A

from jonse.models import Listing


class ListingTable(tables.Table):
    edit = tables.LinkColumn(
        "listing_detail", args=[A("pk")], orderable=False, empty_values=()
    )

    class Meta:
        model = Listing
        template_name = "tables/listing_table.html"
        attrs = {"class": "table table-responsive"}
        fields = (
            "name",
            "jonse_amount",
            "wolse_amount",
            "wolse_rent",
            "monthly_expense",
            "number_of_rooms",
            "number_of_bathrooms",
            "condition",
            "description",
        )

    def render_edit(self, value):
        return "edit"
