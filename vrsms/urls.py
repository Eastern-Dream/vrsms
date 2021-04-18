"""vrsms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import vrsms.views as views
from vrsms.forms import *

urlpatterns = [
    # Django automatically generated admin page
    path('admin/', admin.site.urls),

    path('', views.menu),
    # Customer CRUD path
    path('customer/create',           CustomerCreate.as_view(), name='create_customer'),
    path('customer',                  views.read_customer,      name='read_customer'),
    path('customer/update/<slug:pk>', CustomerUpdate.as_view(), name='update_customer'),
    path('customer/delete/<slug:pk>', CustomerDelete.as_view(), name='delete_customer'),

    # DVD CRUD path
    path('dvd/create',           DvdCreate.as_view(), name='create_dvd'),
    path('dvd',                  views.read_dvd,      name='read_dvd'),
    path('dvd/update/<slug:pk>', DvdUpdate.as_view(), name='update_dvd'),
    path('dvd/delete/<slug:pk>', DvdDelete.as_view(), name='delete_dvd'),

    # Employee CRUD path
    path('employee/create',           EmployeeCreate.as_view(),    name='create_employee'),
    path('employee',                  views.read_employee,      name='read_employee'),
    path('employee/update/<slug:pk>', EmployeeUpdate.as_view(), name='update_employee'),
    path('employee/delete/<slug:pk>', EmployeeDelete.as_view(), name='delete_employee'),

    # Credit Card CRUD path
    path('creditcard/create',           CreditCardCreate.as_view(),    name='create_creditcard'),
    path('creditcard',                  views.read_creditcard,      name='read_creditcard'),
    path('creditcard/update/<slug:pk>', CreditCardUpdate.as_view(), name='update_creditcard'),
    path('creditcard/delete/<slug:pk>', CreditCardDelete.as_view(), name='delete_creditcard'),

    # Rental CRUD path
    path('rental/create',           RentalCreate.as_view(),    name='create_rental'),
    path('rental',                  views.read_rental,      name='read_rental'),
    path('rental/update/<slug:pk>', RentalUpdate.as_view(), name='update_rental'),
    path('rental/delete/<slug:pk>', RentalDelete.as_view(), name='delete_rental'),

    # Request CRUD path
    path('request/create',           RequestCreate.as_view(), name='create_request'),
    path('request',                  views.read_request,      name='read_request'),
    path('request/update/<slug:pk>', RequestUpdate.as_view(), name='update_request'),
    path('request/delete/<slug:pk>', RequestDelete.as_view(), name='delete_request'),

]
