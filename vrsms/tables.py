import django_tables2 as tables
from vrsms.models import *

class CustomerTable(tables.Table):
    update = tables.TemplateColumn('<a href="{% url "update_customer" record.id %}">Click to update</a>')
    delete = tables.TemplateColumn('<a href="{% url "delete_customer" record.id %}">Click to delete</a>')
    class Meta:
        model = Customer

class DvdTable(tables.Table):
    update = tables.TemplateColumn('<a href="{% url "update_dvd" record.id %}">Click to update</a>')
    delete = tables.TemplateColumn('<a href="{% url "delete_dvd" record.id %}">Click to delete</a>')
    class Meta:
        model = Dvd

class EmployeeTable(tables.Table):
    update = tables.TemplateColumn('<a href="{% url "update_employee" record.id %}">Click to update</a>')
    delete = tables.TemplateColumn('<a href="{% url "delete_employee" record.id %}">Click to delete</a>')
    class Meta:
        model = Employee

class CreditCardTable(tables.Table):
    update = tables.TemplateColumn('<a href="{% url "update_creditcard" record.id %}">Click to update</a>')
    delete = tables.TemplateColumn('<a href="{% url "delete_creditcard" record.id %}">Click to delete</a>')
    class Meta:
        model = CreditCard

class RentalTable(tables.Table):
    update = tables.TemplateColumn('<a href="{% url "update_rental" record.id %}">Click to update</a>')
    delete = tables.TemplateColumn('<a href="{% url "delete_rental" record.id %}">Click to delete</a>')
    class Meta:
        model = Rental

class RequestTable(tables.Table):
    update = tables.TemplateColumn('<a href="{% url "update_request" record.id %}">Click to update</a>')
    delete = tables.TemplateColumn('<a href="{% url "delete_request" record.id %}">Click to delete</a>')
    class Meta:
        model = Request