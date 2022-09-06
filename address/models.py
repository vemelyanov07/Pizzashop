from django.db import models
from django.conf import settings

# Create your models here.


class Address(models.Model):
    customer = models.CharField(max_length=50)
    postal_code = models.BigIntegerField(null=False)
    address_name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)

