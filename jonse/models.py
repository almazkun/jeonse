from django.db import models

from jonse.colors import get_pair


def default_listing_name():
    while True:
        name = get_pair().title()[:200]
        if not Listing.objects.filter(name=name).exists():
            return name


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    deleted_on = models.BooleanField(default=False)

    class Meta:
        abstract = True


class ListingManager(models.Manager):
    def for_home(self):
        return self.filter(deleted_on=False).order_by("-created_at")


# Create your models here.
class Listing(BaseModel):
    NEW = 0
    OK = 1
    OLD = 2

    condition_choices = (
        (NEW, "New"),
        (OK, "OK"),
        (OLD, "Old"),
    )

    name = models.CharField(max_length=200, default=default_listing_name)

    jonse_amount = models.IntegerField(default=0)

    wolse_amount = models.IntegerField(default=0)

    wolse_rent = models.IntegerField(default=0)
    gwanlibi = models.IntegerField(default=0)

    jonse_interest_rate = models.FloatField(default=4)
    jonse_interest_amount_per_month = models.IntegerField(default=0)

    monthly_expense = models.IntegerField(default=0)

    number_of_rooms = models.SmallIntegerField(default=1)
    number_of_bathrooms = models.SmallIntegerField(default=1)

    condition = models.SmallIntegerField(choices=condition_choices, default=OK)

    description = models.TextField(blank=True)

    objects = ListingManager()

    def save(self, *args, **kwargs):
        self.jonse_interest_amount_per_month = int(
            self.jonse_amount * self.jonse_interest_rate / 100
        )
        self.monthly_expense = int(
            self.wolse_rent + self.gwanlibi + self.jonse_interest_amount_per_month
        )
        return super().save(*args, **kwargs)

    """
from jonse.models import Listing
Listing.objects.all().delete()
from random import choice
for i in range(100):
    Listing.objects.create(
        jonse_amount=choice(range(0, 1000000))*i,
        wolse_amount=choice(range(0, 1000000))*i,
        wolse_rent=choice(range(0, 100000))*i,
        gwanlibi=choice(range(0, 100000))*i,
        number_of_rooms=choice(range(1, 10)),
        number_of_bathrooms=choice(range(1, 10)),
        condition=choice(range(0, 3)),
        description=i,
    )
    """
