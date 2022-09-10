from django.db import models
from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('email field should be filled')
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)



    def create_user(self, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(self, password,  **extra_fields)


    def  create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user(self, password,  **extra_fields)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=Ttue')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=Ttue')
        


        





class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', unique=True)
    first_name=models.CharField('name', max_length=30, blank=True)
    last_name=models.CharField('surname', max_length=30, blank=True)
    date_joned=models.DateTimeField('date joned', auto_now_add=True)
    avatar=models.ImageField(upload_to='avatars/', null=True, blank = True)


    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=[]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


#class Profile(models.Model):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    #photo = models.ImageField(upload_to=f"users/", blank=True)
    #email = models.EmailField(blank=True)

   # def __str__(self):
       # return f"{self.user.username}'s Profile."
