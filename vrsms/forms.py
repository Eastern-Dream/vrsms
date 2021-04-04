from django.forms import ModelForm
from vrsms.models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class DvdForm(ModelForm):
    class Meta:
        model = Dvd
        fields = '__all__'

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class DvdForm(ModelForm):
    class Meta:
        model = Dvd
        fields = '__all__'

class Administrator(ModelForm):
    class Meta:
        model = Administrator
        fields = '__all__'

class CreditCardForm(ModelForm):
    class Meta:
        model = CreditCard
        fields = '__all__'

class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = '__all__'

