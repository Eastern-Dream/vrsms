from django.urls import reverse_lazy
from django.forms import ModelForm
from django.views.generic.edit import *
from vrsms.models import *

# CUD only, no R form as it has to be handled differently
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

# Credit Card CUD Form
class CreditCardCreate(CreateView):
    template_name = 'create.html'
    model = CreditCard
    fields = '__all__'
    success_url = reverse_lazy('read_creditcard')

class CreditCardUpdate(UpdateView):
    template_name = 'update.html'
    model = CreditCard
    fields = '__all__'
    success_url = reverse_lazy('read_creditcard')

class CreditCardDelete(DeleteView):
    template_name = 'delete.html'
    model = CreditCard
    success_url = reverse_lazy('read_creditcard')

# Rental CUD Form
class RentalCreate(CreateView):
    template_name = 'create.html'
    model = Rental
    fields = '__all__'
    success_url = reverse_lazy('read_rental')

class RentalUpdate(UpdateView):
    template_name = 'update.html'
    model = Rental
    fields = '__all__'
    success_url = reverse_lazy('read_rental')

class RentalDelete(DeleteView):
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