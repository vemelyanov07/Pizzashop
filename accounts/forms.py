from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = ('photo', 'username', 'user', 'email')
