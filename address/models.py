from django.db import models

class Address(models.Model):
    customer = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    address_name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    landmark = models.CharField(max_length=50) 
    is_deleted = models.BooleanField()  

    def __str__(self):
        return self.customer

