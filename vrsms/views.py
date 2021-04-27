from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from vrsms.models import *
from vrsms.tables import *
from vrsms.forms import *

# Main Menu view
def menu(request):
    return render(request, "menu.html")


# Logout view
def user_logout(request):
    # Simply call logout method defined by Django to logout any users
    logout(request)
    # Redirect user back to main menu, which requires a login in the first place
    return redirect('/')


# Special case for all read views because we need to construct a table and pass that through to the template
# For each read views, context is where we construct a table then pass the variable context to render method
def read_customer(request):
    context = {'table': CustomerTable(Customer.objects.all()), 'entity':"customer"}
    return render(request, "read.html", context)

def read_dvd(request):
    context = {'table': DvdTable(Dvd.objects.all()), 'entity':"dvd"}
    return render(request, "read.html", context)

# For read employee, we have to check if the user has the correct permission, if not we return a 403 forbidden with error message
def read_employee(request):
    if request.user.has_perm('vrsms.view_employee'):
        context = {'table': EmployeeTable(Employee.objects.all()), 'entity':"employee"}
        return render(request, "read.html", context)
    else:
        return HttpResponseForbidden('Only the Owner have access to the Employee table.')

def read_rental(request):
    context = {'table': RentalTable(Rental.objects.all()), 'entity':"rental"}
    return render(request, "read.html", context)

def read_request(request):
    context = {'table': RequestTable(Request.objects.all()), 'entity':"request"}
    return render(request, "read.html", context)


# Special case for creating a rental object view because it need to be explicitly defined in order to do form validation
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

# Special case for creating a sell object view because it need to be explicitly defined in order to do form validation
def sell_dvd(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SellForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SellForm()
    return render(request, 'create.html', {'form': form})
