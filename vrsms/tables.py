import django_tables2 as tables
from django_tables2 import A
from vrsms.models import *
app_name = 'vrsms'


class CustomerTable(tables.Table):
    update = tables.TemplateColumn('<a href="{% url "update_customer" record.id %}">Click to edit</a>')
    delete = tables.TemplateColumn('<a href="{% url "delete_customer" record.id %}">Click to delete</a>')
    class Meta:
        model = Customer


