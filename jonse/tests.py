from random import choice as c

from django.test import TestCase

from jonse.models import Listing


# Create your tests here.
class TestModels(TestCase):
    def test_listing(self):
        possible_numbers = [
            -1,
            0,
            100,
            1000,
        ]
        for i in range(100):

            l_data = {
                "jonse_amount": c(possible_numbers),
                "wolse_amount": c(possible_numbers),
                "wolse_rent": c(possible_numbers),
                "gwanlibi": c(possible_numbers),
                "jonse_interest_rate": c(possible_numbers),
            }

            listing = Listing.objects.create(**l_data)

            jonse_interest_amount_per_month = int(
                l_data["jonse_amount"] * l_data["jonse_interest_rate"] / 100
            )

            monthly_expense = int(
                l_data["wolse_rent"]
                + l_data["gwanlibi"]
                + jonse_interest_amount_per_month
            )

            self.assertEqual(
                listing.jonse_interest_amount_per_month, jonse_interest_amount_per_month
            )

            self.assertEqual(listing.monthly_expense, monthly_expense)
