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

    def setUp(self):
        self.client = Client()
        self.user_data_0 = {
            "email": "test_user@email.com",
            "password": "testpassword",
        }
        self.user_data_1 = {
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
        for i in range(number):
            l_data = self.listing_data.copy()
            l_data["creator"] = get_user_model().objects.get(
                email=email,
            )
            Listing.objects.create(**l_data)

    def test_home_view(self):
        n_one = 3
        n_two = 4

        self._signup(self.user_data_0.get("email"), self.user_data_0.get("password"))
        self._signup(self.user_data_1.get("email"), self.user_data_1.get("password"))
        self._create_listings(self.user_data_0.get("email"), n_one)
        self._create_listings(self.user_data_1.get("email"), n_two)

        c = self.client
        r = c.get(reverse("home"))

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.context["object_list"].count(), n_one + n_two)

    def test_my_listing_view(self):
        c = self.client
        r = c.get(reverse("my_listings"))

        self.assertEqual(r.status_code, 302)

        self._signup(self.user_data_0.get("email"), self.user_data_0.get("password"))
        c.login(**self.user_data_0)
        r = c.get(reverse("my_listings"))

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.context["object_list"].count(), 0)

        self._create_listings(self.user_data_0.get("email"), 10)
        self._signup(self.user_data_1.get("email"), self.user_data_1.get("password"))
        self._create_listings(self.user_data_1.get("email"), 10)

        r = c.get(reverse("my_listings"))

        self.assertEqual(r.context["object_list"].count(), 10)
        self.assertTrue(
            all(
                [
                    listing.creator.email == self.user_data_0.get("email")
                    for listing in r.context["object_list"]
                ]
            )
        )

    def test_listing_create_view(self):
        c = self.client
        r = c.get(reverse("listing_create"))

        self.assertEqual(r.status_code, 302)

        self._signup(self.user_data_0.get("email"), self.user_data_0.get("password"))
        c.login(**self.user_data_0)
        r = c.get(reverse("listing_create"))

        self.assertEqual(r.status_code, 200)

        data = self.listing_data.copy()
        data.update(
            {
                "name": "some name",
                "number_of_rooms": 1,
                "number_of_bathrooms": 1,
                "condition": 1,
            }
        )
        r = c.post(reverse("listing_create"), data=data)

        self.assertEqual(r.status_code, 302)
        self.assertEqual(
            Listing.objects.get(**self.listing_data).creator.email,
            self.user_data_0.get("email"),
        )

    def test_listing_detail_view(self):
        c = self.client
        pk = 10

        self._signup(self.user_data_0.get("email"), self.user_data_0.get("password"))
        self._create_listings(self.user_data_0.get("email"), pk)

        r = c.get(
            reverse("listing_detail", kwargs={"pk": pk}),
        )

        self.assertEqual(r.status_code, 302)
        self.assertTrue(r.url.startswith(reverse("account_login")))

        listing = Listing.objects.get(pk=pk)
        r = c.get(
            reverse("listing_detail", kwargs={"pk": listing.pk}),
        )

        self.assertEqual(r.status_code, 302)
        self.assertTrue(r.url.startswith(reverse("account_login")))

        c.login(**self.user_data_0)
        r = c.get(
            reverse("listing_detail", kwargs={"pk": listing.pk}),
        )

        self.assertEqual(r.status_code, 200)
        self.assertTrue(listing.name in str(r.content))

    def test_listing_update_view(self):
        c = self.client
        pk = 10

        self._signup(self.user_data_0.get("email"), self.user_data_0.get("password"))
        self._create_listings(self.user_data_0.get("email"), pk)
        r = c.get(
            reverse("listing_update", kwargs={"pk": pk}),
        )

        self.assertEqual(r.status_code, 302)
        self.assertTrue(r.url.startswith(reverse("account_login")))

        listing = Listing.objects.get(pk=pk)
        r = c.get(
            reverse("listing_update", kwargs={"pk": listing.pk}),
        )

        self.assertEqual(r.status_code, 302)
        self.assertTrue(r.url.startswith(reverse("account_login")))

        c.login(**self.user_data_0)
        r = c.get(
            reverse("listing_update", kwargs={"pk": listing.pk}),
        )

        self.assertEqual(r.status_code, 200)
        self.assertTrue(listing.name in str(r.content))

        r = c.post(
            reverse("listing_update", kwargs={"pk": listing.pk}), data=self.updated_data
        )

        self.assertEqual(r.status_code, 302)
        self.assertTrue(Listing.objects.filter(**self.updated_data).exists())

    def test_listing_delete_view(self):
        c = self.client
        pk = 10

        self._signup(self.user_data_0.get("email"), self.user_data_0.get("password"))
        self._create_listings(self.user_data_0.get("email"), pk)
        r = c.get(
            reverse("listing_delete", kwargs={"pk": pk}),
        )

        self.assertEqual(r.status_code, 302)
        self.assertTrue(r.url.startswith(reverse("account_login")))

        listing = Listing.objects.get(pk=pk)
        r = c.get(
            reverse("listing_delete", kwargs={"pk": listing.pk}),
        )

        self.assertEqual(r.status_code, 302)
        self.assertTrue(r.url.startswith(reverse("account_login")))

        c.login(**self.user_data_0)
        r = c.get(
            reverse("listing_delete", kwargs={"pk": listing.pk}),
        )

        self.assertEqual(r.status_code, 200)
        self.assertTrue(listing.name in str(r.content))

        r = c.post(
            reverse("listing_delete", kwargs={"pk": listing.pk}),
        )

        self.assertEqual(r.status_code, 302)
        self.assertFalse(Listing.objects.filter(pk=pk).exists())
