from django.forms import ModelForm

from jeonse.models import Listing


class ListingCreateForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            "name",
            "jeonse_amount",
            "wolse_amount",
            "wolse_rent",
            "gwanlibi",
            "jeonse_interest_rate",
            "number_of_rooms",
            "number_of_bathrooms",
            "condition",
            "description",
        ]
