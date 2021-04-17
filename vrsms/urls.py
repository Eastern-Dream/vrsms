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

    # Customer CRUD path
    path('customer/create',          views.create_customer,    name='create_customer'),
    path('customer',                 views.read_customer,      name='read_customer'),
    path('customer/update/<slug:pk>', CustomerUpdate.as_view(), name='update_customer'),
    path('customer/delete/<slug:pk>', CustomerDelete.as_view(), name='delete_customer'),
    # path('delete/<int:id>', views.delete_customer),

]
