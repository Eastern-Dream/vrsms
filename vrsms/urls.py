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
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Django automatically generated admin page
    path('admin/', admin.site.urls),

    # Login/Logout path
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', views.user_logout, name='logout'),

    # Main Menu
    path('', login_required(views.menu), name='menu'),

    # Customer CRUD path
    path('customer/create',           login_required(CustomerCreate.as_view()), name='create_customer'),
    path('customer',                  login_required(views.read_customer),      name='read_customer'),
    path('customer/update/<slug:pk>', login_required(CustomerUpdate.as_view()), name='update_customer'),
    path('customer/delete/<slug:pk>', login_required(CustomerDelete.as_view()), name='delete_customer'),

    # DVD CRUD path
    path('dvd/create',                login_required(DvdCreate.as_view()),      name='create_dvd'),
    path('dvd',                       login_required(views.read_dvd),           name='read_dvd'),
    path('dvd/update/<slug:pk>',      login_required(DvdUpdate.as_view()),      name='update_dvd'),
    path('dvd/delete/<slug:pk>',      login_required(DvdDelete.as_view()),      name='delete_dvd'),

    # Employee CRUD path
    path('employee/create',           login_required(EmployeeCreate.as_view()), name='create_employee'),
    path('employee',                  login_required(views.read_employee),      name='read_employee'),
    path('employee/update/<slug:pk>', login_required(EmployeeUpdate.as_view()), name='update_employee'),
    path('employee/delete/<slug:pk>', login_required(EmployeeDelete.as_view()), name='delete_employee'),

    # Rental CRUD path
    path('rental/create',             login_required(views.create_rental),      name='create_rental'),
    path('rental',                    login_required(views.read_rental),        name='read_rental'),
    path('rental/update/<slug:pk>',   login_required(RentalUpdate.as_view()),   name='update_rental'),
    path('rental/return/<slug:pk>',   login_required(RentalReturn.as_view()),   name='return_rental'),

    # Request CRUD path
    path('request/create',            login_required(RequestCreate.as_view()),  name='create_request'),
    path('request',                   login_required(views.read_request),       name='read_request'),
    path('request/update/<slug:pk>',  login_required(RequestUpdate.as_view()),  name='update_request'),
    path('request/delete/<slug:pk>',  login_required(RequestDelete.as_view()),  name='delete_request'),

    # URL path to sell DVD
    path('sell', login_required(views.sell_dvd), name='sell_dvd')
]
