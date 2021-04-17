from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from vrsms.forms import *
from vrsms.models import *
from vrsms.tables import *
from typing import List
from typing import Dict

# Create group
def create_customer(request):
    form = None
    if request.method == "POST":
        form = CustomerForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            try:
                form.save()
                return redirect('/customer')
            except:
                return redirect('/')
    else:
        form = CustomerForm()
    return render(request, "create.html", {'form':form, 'entity':"Customer"})

# Read group
def read_customer(request):
    context = {'table':CustomerTable(Customer.objects.all())}
    return render(request, "read.html", context)

# Update group
def update_customer(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerUpdate(request.POST, instance = customer)
    form
    if form.is_valid():
        form.save()
        return redirect("/customer")
    return render(request, 'update.html', {'form':form, 'entity':"Customer"})

# Delete Group
def delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("/customer")

# def make_readable_fields(fields: List, prefix='') -> List:
#     result = []
#     for field in fields:
#         readable = prefix + ' '
#         for word in field.split('_'):
#             if word == 'id':
#                 readable += word.upper() + ' '
#             else:
#                 readable += word.capitalize() + ' '
#         result.append(readable.strip())
#     return result

# def construct_read_context(object, prefix='') -> Dict:
#     fields = [field.name for field in object._meta.fields]
#     query = object.objects.all()
#     readable_fields = make_readable_fields(fields, prefix)
#     context = {'query':query, 'readable_fields':readable_fields}
#     return context


# def construct_create_context(object, prefix='') -> Dict:
#     fields = [field.name for field in object._meta.fields]
#     fields = fields[1:]
#     readable_fields = make_readable_fields(fields, prefix)
#     all_fields = zip(fields, readable_fields)
#     context = {'fields':all_fields}
#     return context
