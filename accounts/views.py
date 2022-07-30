from django.views.generic import TemplateView


class LoginPageView(TemplateView):
    template_name = 'accounts/login.html'
    
    
class RegistrationPageView(TemplateView):
    template_name = 'accounts/registration.html'
