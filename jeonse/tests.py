from random import choice as c

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from jeonse.models import Listing


# Create your tests here.
class TestModels(TestCase):
    def test_listing(self):
        creator = get_user_model().objects.create(
            username="someusername",
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
    def _signup(self, email, password) -> "response":
        return Client().post(
            reverse("account_signup"),
            {
                "email": email,
                "password1": password,
                "password2": password,
            },
        )

    def _login(self, email, password) -> "response":
        return self.client.post(
            reverse("account_login"),
            {
                "email": email,
                "password": password,
            },
        )

    def _logout(self) -> "response":
        return self.client.post(
            reverse("account_logout"),
        )

    def setUp(self):
        self.client = Client()
        self.user_data = {
            "email": "test_user@email.com",
            "password": "testpassword",
        }
        self.other_user_data = {
            "email": "other_test_user@email.com",
            "password": "testpassword",
        }
        self.listing_data = {
            "jeonse_amount": 100,
            "wolse_amount": 100,
            "wolse_rent": 100,
            "gwanlibi": 100,
            "jeonse_interest_rate": 100,
        }
        self.updated_data = {
            "name": "new awesome name",
            "jeonse_amount": 10,
            "wolse_amount": 10,
            "wolse_rent": 10,
            "gwanlibi": 10,
            "jeonse_interest_rate": 10,
            "number_of_rooms": 10,
            "number_of_bathrooms": 10,
            "condition": 2,
        }

    def _create_listings(self, email, number: int):
        print(email)
        for i in range(number):
            l_data = self.listing_data.copy()
            l_data["creator"] = get_user_model().objects.get(
            email=email,
        )
            Listing.objects.create(**l_data)

    def test_my_listing_view(self):
        response = self.client.get(reverse("my_listings"))
        # test LoginRequiredMixin
        self.assertEqual(response.status_code, 302)

        self._signup(self.user_data.get("email"), self.user_data.get("password"))
        self._login(self.user_data.get("email"), self.user_data.get("password"))

        response = self.client.get(reverse("my_listings"))
        self.assertEqual(response.status_code, 200)

        # test queryset only contains user's listings
        self.assertEqual(response.context["object_list"].count(), 0)

        self._create_listings(self.user_data.get("email"), 10)

        self._signup(self.other_user_data.get("email"), self.other_user_data.get("password"))
        self._create_listings(self.other_user_data.get("email"), 10)

        response = self.client.get(reverse("my_listings"))
        self.assertEqual(response.context["object_list"].count(), 10)
        """
    def test_listing_create_view(self):
        c = Client()
        response = c.get(reverse("listing_create"))

        self.assertEqual(response.status_code, 302)

        c.force_login(self.user)
        response = c.get(reverse("listing_create"))
        self.assertEqual(response.status_code, 200)

        data = self.listing_data
        data.update(
            {
                "name": "some name",
                "number_of_rooms": 1,
                "number_of_bathrooms": 1,
                "condition": 1,
            }
        )

        response = c.post(reverse("listing_create"), data=data)
        self.assertEqual(response.status_code, 302)
        listing = Listing.objects.get(**self.listing_data)
        self.assertEqual(listing.creator, self.user)

    def test_listing_detail_view(self):
        c = Client()

        pk = 10

        self._create_listings(self.user, pk)

        response = c.get(
            reverse("listing_detail", kwargs={"pk": pk}),
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("account_login")))

        listing = Listing.objects.get(pk=pk)

        response = c.get(
            reverse("listing_detail", kwargs={"pk": listing.pk}),
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("account_login")))

        c.force_login(self.user)

        response = c.get(
            reverse("listing_detail", kwargs={"pk": listing.pk}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(listing.name in str(response.content))

    def test_listing_update_view(self):
        c = Client()
        pk = 10

        self._create_listings(self.user, pk)

        response = c.get(
            reverse("listing_update", kwargs={"pk": pk}),
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("account_login")))

        listing = Listing.objects.get(pk=pk)

        response = c.get(
            reverse("listing_update", kwargs={"pk": listing.pk}),
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("account_login")))

        c.force_login(self.user)

        response = c.get(
            reverse("listing_update", kwargs={"pk": listing.pk}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(listing.name in str(response.content))

        response = c.post(
            reverse("listing_update", kwargs={"pk": listing.pk}), data=self.updated_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Listing.objects.filter(**self.updated_data).exists())

    def test_listing_delete_view(self):
        c = Client()
        pk = 10

        self._create_listings(self.user, pk)

        response = c.get(
            reverse("listing_delete", kwargs={"pk": pk}),
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("account_login")))

        listing = Listing.objects.get(pk=pk)

        response = c.get(
            reverse("listing_delete", kwargs={"pk": listing.pk}),
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("account_login")))

        c.force_login(self.user)

        response = c.get(
            reverse("listing_delete", kwargs={"pk": listing.pk}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(listing.name in str(response.content))

        response = c.post(
            reverse("listing_delete", kwargs={"pk": listing.pk}),
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Listing.objects.filter(pk=pk).exists())

        """
