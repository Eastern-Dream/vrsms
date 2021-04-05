import django_tables2 as tables
from vrsms.models import *

class CustomerTable(tables.Table):
    class Meta:
        model = Customer
