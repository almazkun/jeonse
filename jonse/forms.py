from django.forms import ModelForm

from jonse.models import Listing


class ListingCreateForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            "name",
            "jonse_amount",
            "wolse_amount",
            "wolse_rent",
            "gwanlibi",
            "jonse_interest_rate",
            "number_of_rooms",
            "number_of_bathrooms",
            "condition",
            "description",
        ]
