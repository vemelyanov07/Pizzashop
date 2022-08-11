from django.views.generic import TemplateView

class ChangeAddressPageView(TemplateView):
    template_name = 'address/change_address.html'

class AddressPageView(TemplateView):
    template_name = 'address/address.html'

