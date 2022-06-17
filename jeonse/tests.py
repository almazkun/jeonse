from random import choice as c

from django.test import Client, TestCase
from django.urls import reverse

from apps.accounts.models import CustomUser
from jeonse.models import Listing


# Create your tests here.
class TestModels(TestCase):
    def test_listing(self):
        creator = CustomUser.objects.create(
            email="some@email.com",
        )
        possible_numbers = [
            -1,
            0,
            100,
            1000,
        ]
        for i in range(100):

            l_data = {
                "creator": creator,
                "jeonse_amount": c(possible_numbers),
                "wolse_amount": c(possible_numbers),
                "wolse_rent": c(possible_numbers),
                "gwanlibi": c(possible_numbers),
                "jeonse_interest_rate": c(possible_numbers),
            }

            listing = Listing.objects.create(**l_data)

            jeonse_interest_amount_per_month = int(
                l_data["jeonse_amount"] * l_data["jeonse_interest_rate"] / 100 / 12
            )

            monthly_expense = int(
                l_data["wolse_rent"]
                + l_data["gwanlibi"]
                + jeonse_interest_amount_per_month
            )

            self.assertEqual(
                listing.jeonse_interest_amount_per_month,
                jeonse_interest_amount_per_month,
            )

            self.assertEqual(listing.monthly_expense, monthly_expense)


class TestViews(TestCase):
    def setUp(self):
        user_data = {
            "email": "testuser@email.com",
            "password": "testpassword",
        }

        self.user = CustomUser.objects.create(email=user_data.get("email"))
        self.user.set_password(user_data.get("password"))
        self.user.save()

        self.other_user = CustomUser.objects.create(email="other@user.com")

        self.listing_data = {
            "jeonse_amount": 100,
            "wolse_amount": 100,
            "wolse_rent": 100,
            "gwanlibi": 100,
            "jeonse_interest_rate": 100,
        }

    def _create_listings(self, user, number: int):
        for i in range(number):
            l_data = self.listing_data.copy()
            l_data["creator"] = user
            Listing.objects.create(**l_data)

    def test_my_listing_view(self):
        c = Client()
        response = c.get(reverse("my_listings"))
        # test LoginRequiredMixin
        self.assertEqual(response.status_code, 302)

        c.force_login(self.user)

        response = c.get(reverse("my_listings"))
        self.assertEqual(response.status_code, 200)

        # test queryset only contains user's listings
        self.assertEqual(response.context["object_list"].count(), 0)

        self._create_listings(self.user, 10)
        self._create_listings(self.other_user, 10)

        response = c.get(reverse("my_listings"))
        self.assertEqual(response.context["object_list"].count(), 10)

    def test_listing_create_view(self):
        c = Client()
        response = c.get(reverse("listing_create"))
        # test LoginRequiredMixin
        self.assertEqual(response.status_code, 302)

        c.force_login(self.user)

        response = c.get(reverse("listing_create"))
        self.assertEqual(response.status_code, 200)

        data = response.context["form"]
        print(data)
        data.update(self.listing_data)

        print(data)
        # test form
        response = c.post(reverse("listing_create"), data=data)
        self.assertEqual(response.status_code, 200)
        print(response.context["form"].errors)
        self.assertTrue(response.context["form"].is_valid())

        self.assertFalse(response.context["form"].errors)

        listing = Listing.objects.get(**self.listing_data)
        self.assertEqual(listing.creator, self.user)
