from django.shortcuts import render, redirect
from vrsms.forms import *
from vrsms.models import *
from typing import List
from typing import Dict

# def customer(request):
#     if request.method == "POST":
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/show')
#             except:
#                 pass
#     else:
#         form = CustomerForm()
#     return render(request,'index.html',{'form':form})

# Read group
def read_customer(request):
    context = construct_read_context(Customer, 'Customer')
    return render(request, "read.html", context)

# def read_employee(request):
#     customers = Customer.objects.all()
#     return render(request, "customer.html", {'customers':customers})


# def read_dvd(request):
#     customers = Customer.objects.all()
#     return render(request, "customer.html", {'customers':customers})


# def read_administrator(request):
#     customers = Customer.objects.all()
#     return render(request, "customer.html", {'customers':customers})


# def read_creditcard(request):
#     customers = Customer.objects.all()
#     return render(request, "customer.html", {'customers':customers})


# def read_rental(request):
#     customers = Customer.objects.all()
#     return render(request, "customer.html", {'customers':customers})


# def read_request(request):
#     customers = Customer.objects.all()
#     return render(request, "customer.html", {'customers':customers})


# def edit(request, id):
#     customer = Customer.objects.get(id=id)
#     return render(request,'edit.html', {'customer':customer})


# def update(request, id):
#     customer = Customer.objects.get(id=id)
#     form = CustomerForm(request.POST, instance = customer)

#     if form.is_valid():
#         form.save()
#         return redirect("/show")
#     return render(request, 'edit.html', {'customer': customer})


# def delete(request, id):
#     customer = Customer.objects.get(id=id)
#     customer.delete()
#     return redirect("/show")



def construct_read_context(object, prefix='') -> Dict:

    def readable_fields(fields: List, prefix='') -> List:
        result = []
        for field in fields:
            readable = prefix + ' '
            for word in field.split('_'):
                if word == 'id':
                    readable += word.upper() + ' '
                else:
                    readable += word.capitalize() + ' '
            result.append(readable.strip())
        return result
    
    fields = [field.name for field in object._meta.fields]
    query = zip(object.objects.all(), fields)
    readable_fields = readable_fields(fields, prefix)
    context = {'query':query, 'readable_fields':readable_fields}
    return context

