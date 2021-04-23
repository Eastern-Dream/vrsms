from django.shortcuts import render, redirect
from vrsms.models import *
from vrsms.tables import *
from vrsms.forms import *

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

def read_rental(request):
    context = {'table': RentalTable(Rental.objects.all()), 'entity':"rental"}
    return render(request, "read.html", context)

def read_request(request):
    context = {'table': RequestTable(Request.objects.all()), 'entity':"request"}
    return render(request, "read.html", context)

def create_rental(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RentalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/rental')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RentalForm()
    return render(request, 'create.html', {'form': form})