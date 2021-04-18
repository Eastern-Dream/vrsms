from django.shortcuts import render, redirect
from vrsms.models import *
from vrsms.tables import *

# Main Menu
def menu(request):
    return render(request, "menu.html")

# Read group
def read_customer(request):
    context = {'table': CustomerTable(Customer.objects.all()), 'entity':"customer"}
    return render(request, "read.html", context)

def read_dvd(request):
    context = {'table': DvdTable(Dvd.objects.all()), 'entity':"dvd"}
    return render(request, "read.html", context)

def read_employee(request):
    context = {'table': EmployeeTable(Employee.objects.all()), 'entity':"employee"}
    return render(request, "read.html", context)

def read_creditcard(request):
    context = {'table': CreditCardTable(CreditCard.objects.all()), 'entity':"creditcard"}
    return render(request, "read.html", context)

def read_rental(request):
    context = {'table': RentalTable(Rental.objects.all()), 'entity':"rental"}
    return render(request, "read.html", context)

def read_request(request):
    context = {'table': RequestTable(Request.objects.all()), 'entity':"request"}
    return render(request, "read.html", context)