from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserForm(forms.ModelForms):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileForm(forms.ModelForms):

    class Meta:
        model = Profile
        field = ('photo', 'username', 'user', 'email')