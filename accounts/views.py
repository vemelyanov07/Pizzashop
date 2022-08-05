from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import is_valid_path
from .forms import UserForm
from .forms import Profile
from django.contrib.auth.decorators import login_required
import os


# class RegisterPageView(TemplateView):
#     template_name = ''

class ProfilePageView(TemplateView):
    template_name = 'accounts/profile.html'

class LoginPageView(TemplateView):
    template_name = 'accounts/login.html'
    
class RegistrationPageView(TemplateView):
    template_name = 'accounts/registration.html'
