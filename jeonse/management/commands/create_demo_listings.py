from random import choice

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from jeonse.models import Listing


class Command(BaseCommand):
    help = "Creates Demo Listings"

    def handle(self, *args, **kwargs):
        get_user_model()
        if not get_user_model().objects.filter(email=settings.DEMO_USER_EMAIL).exists():
            self.stdout.write(self.style.ERROR("Demo user does not exist! exiting..."))
            return

        user = get_user_model().objects.get(email=settings.DEMO_USER_EMAIL)
        jeonse_amount_list = [
            0,
            500000000,
            1000000000,
            1500000000,
            2000000000,
            3000000000,
        ]
        wolse_amount_list = [
            0,
            100000000,
            200000000,
            300000000,
            400000000,
            500000000,
        ]
        wolse_rent_list = [
            500000,
            1000000,
            1500000,
            2000000,
            2500000,
        ]
        gwanlibi_list = [
            100000,
            150000,
            200000,
            250000,
            300000,
        ]
        jeonse_interest_rate_list = [
            1,
            1.5,
            2,
            2.5,
            3,
        ]
        number_of_rooms_list = [
            1,
            2,
            3,
            4,
            5,
        ]
        number_of_bathrooms_list = [
            1,
            2,
            3,
            4,
            5,
        ]
        condition_list = [
            0,
            1,
            2,
        ]
        description_list = [
            "https://new.land.naver.com/complexes/451?ms=37.5068059,127.0076982,15&a=APT:ABYG:JGC&e=RETAIL",
            "https://new.land.naver.com/complexes/103501?ms=37.6497795,127.0140628,16&a=APT:ABYG:JGC&e=RETAIL",
            "https://new.land.naver.com/complexes/27378?ms=37.5599897,126.9835531,17&a=APT:ABYG:JGC&e=RETAIL",
            "https://new.land.naver.com/complexes/13147?ms=37.5212879,126.9188521,16&a=APT:ABYG:JGC&e=RETAIL",
            "https://new.land.naver.com/complexes/11489?ms=37.4914246,126.9926633,17&a=APT:ABYG:JGC&e=RETAIL",
        ]

        for i in range(17):
            listing = Listing.objects.create(
                creator=user,
                jeonse_amount=choice(jeonse_amount_list),
                wolse_amount=choice(wolse_amount_list),
                wolse_rent=choice(wolse_rent_list),
                gwanlibi=choice(gwanlibi_list),
                jeonse_interest_rate=choice(jeonse_interest_rate_list),
                number_of_rooms=choice(number_of_rooms_list),
                number_of_bathrooms=choice(number_of_bathrooms_list),
                condition=choice(condition_list),
                description=choice(description_list),
            )
            self.stdout.write(self.style.SUCCESS(f"Demo Listing created: {listing}"))
        self.stdout.write(
            self.style.SUCCESS(f"Demo Listings created: {Listing.objects.count()}")
        )
