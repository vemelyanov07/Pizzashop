from django.db import models
from django.conf import settings
from accounts.models import User
# Create your models here.


class Address(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    postal_code = models.BigIntegerField(null=False)
    address_name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)

    verbose_name_plural = 'Addresses'


