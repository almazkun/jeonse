from django.db import models


# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=200)
    jonse_amount = models.IntegerField(default=0)
    wolse_amount = models.IntegerField(default=0)
    monthly_rent = models.IntegerField(default=0)
    kollibi = models.IntegerField(default=0)
