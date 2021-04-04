from django.forms import ModelForm
from vrsms.models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        # fields = ['first_name', 'last_name', 'license_id', 'birth_date',
        #           'home_address', 'phone_number', 'email_address']
        fields = '__all__'
