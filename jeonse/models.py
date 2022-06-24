from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from jeonse.colors import get_pair


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

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    name = models.CharField(_("Name"), max_length=200, default=default_listing_name)

    jeonse_amount = models.BigIntegerField(_("Jeonse"), default=0)

    wolse_amount = models.BigIntegerField(_("Wolse"), default=0)

    wolse_rent = models.IntegerField(_("Wolse rent"), default=0)
    gwanlibi = models.IntegerField(_("Management fees"), default=0)

    jeonse_interest_rate = models.FloatField(_("Jeonse loan interest rate"), default=4)
    jeonse_interest_amount_per_month = models.IntegerField(
        _("Jeonse loan monthly payment amount"), default=0
    )

    monthly_expense = models.IntegerField(_("Monthly expenses"), default=0)

    number_of_rooms = models.SmallIntegerField(_("# of rooms"), default=1)
    number_of_bathrooms = models.SmallIntegerField(_("# of bathrooms"), default=1)

    condition = models.SmallIntegerField(
        _("Condition"), choices=condition_choices, default=OK
    )

    description = models.TextField(_("Notes"), blank=True)

    objects = ListingManager()

    def save(self, *args, **kwargs):
        self.jeonse_interest_amount_per_month = self.monthly_interest_payment_amount
        self.monthly_expense = self.total_monthly_payment_amount
        return super().save(*args, **kwargs)

    @property
    def annual_interest_payment_amount(self):
        return int(self.jeonse_amount * self.jeonse_interest_rate / 100)

    @property
    def monthly_interest_payment_amount(self):
        return int(self.annual_interest_payment_amount / 12)

    @property
    def total_monthly_payment_amount(self):
        return int(
            self.wolse_rent + self.gwanlibi + self.monthly_interest_payment_amount
        )
