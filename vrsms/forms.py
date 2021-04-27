from django.urls import reverse_lazy
from django.forms import ModelForm
from django.views.generic.edit import *
from vrsms.models import *
from django.core.exceptions import ValidationError

# CUD only, no R form as it has to be handled differently
# For each forms, we define the html template to be used, the model the form is based on, 
# the fields we want the form to access, and the redirect URL if the form is submitted successfully
# All forms that specifies a success URL will always redirect user to the respective table view.
# Customer CUD Form
class CustomerCreate(CreateView):
    template_name = 'create.html'
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('read_customer')

class CustomerUpdate(UpdateView):
    template_name = 'update.html'
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('read_customer')

class CustomerDelete(DeleteView):
    template_name = 'delete.html'
    model = Customer
    success_url = reverse_lazy('read_customer')

# DVD CUD Form
class DvdCreate(CreateView):
    template_name = 'create.html'
    model = Dvd
    fields = '__all__'
    success_url = reverse_lazy('read_dvd')

class DvdUpdate(UpdateView):
    template_name = 'update.html'
    model = Dvd
    fields = '__all__'
    success_url = reverse_lazy('read_dvd')

class DvdDelete(DeleteView):
    template_name = 'delete.html'
    model = Dvd
    success_url = reverse_lazy('read_dvd')

# Employee CUD Form
class EmployeeCreate(CreateView):
    template_name = 'create.html'
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('read_employee')

class EmployeeUpdate(UpdateView):
    template_name = 'update.html'
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('read_employee')

class EmployeeDelete(DeleteView):
    template_name = 'delete.html'
    model = Employee
    success_url = reverse_lazy('read_employee')

# Rental CUD Form
# Special rental create form that check for validity like max 3 active rentals and see if DVD is in stock
class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'

    # This clean method is called everytime before a form is submitted to check if the data is valid
    def clean(self):
        # Get the current active rental from the customer selected in the form
        rental_amount = Rental.objects.filter(customer_id=self.cleaned_data['customer_id'])
        # Get the current amount in stock for the DVD selected in the form
        amount_instock = self.cleaned_data['dvd_id'].amount_instock
        # Check if there are zero instock, if there is then raise error message
        if amount_instock == 0:
            raise ValidationError("This DVD is not in stock.")
        # Check if there are 3 active rentals, if there is then raise error message
        if rental_amount.count() == 3:
            raise ValidationError("Customer can only have maximum of 3 active rentals.")
        return self.cleaned_data

class RentalUpdate(UpdateView):
    template_name = 'update.html'
    model = Rental
    fields = '__all__'
    success_url = reverse_lazy('read_rental')

class RentalReturn(DeleteView):
    template_name = 'delete.html'
    model = Rental
    success_url = reverse_lazy('read_rental')

# Request CUD Form
class RequestCreate(CreateView):
    template_name = 'create.html'
    model = Request
    fields = '__all__'
    success_url = reverse_lazy('read_request')

class RequestUpdate(UpdateView):
    template_name = 'update.html'
    model = Request
    fields = '__all__'
    success_url = reverse_lazy('read_request')

class RequestDelete(DeleteView):
    template_name = 'delete.html'
    model = Request
    success_url = reverse_lazy('read_request')

# Special form for selling DVD that checks if the selected DVD in the form is in stock
class SellForm(ModelForm):
    class Meta:
        model = Sell
        fields = '__all__'

    # This clean method is called everytime before a form is submitted to check if the data is valid
    def clean(self):
        # Get the current amount in stock for the DVD selected in the form
        amount_instock = self.cleaned_data['dvd_id'].amount_instock
        # Check if there are zero instock, if there is then raise error message
        if amount_instock == 0:
            raise ValidationError("This DVD is not in stock.")
        return self.cleaned_data