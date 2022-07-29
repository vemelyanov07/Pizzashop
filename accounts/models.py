from django.db import models
from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to=f"users/", blank=True)
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(blank=True)


def __str__(self):
    return f"{self.user.username}'s Profile."
