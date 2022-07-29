from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import is_valid_path
from .forms import UserRegistrationForms, UserForm, ProfileForm
from .forms import Profile
from django.contrib.auth.decorators import login_required
import os



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForms(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'registration/registration_done.html')
        return render(request, 'registration/registration.html',{'user_form': user_form})
    return render(request, 'registration/registration.html',{'user_form': UserRegistrationForms()})


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST, data=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'registration/profile.html', {'user_form':user_form, 
                                            'profile_form': profile_form})

class LoginPageView(TemplateView):
    template_name = 'accounts/login.html'
