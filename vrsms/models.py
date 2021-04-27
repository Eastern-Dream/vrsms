from django.db import models
from django.db.models.signals import *
from django.dispatch import receiver

# Customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    license_id = models.CharField(max_length=200)
    birth_date = models.DateField()
    home_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    card_number = models.CharField(max_length=200)
    card_expire_date = models.DateField()
    # Custom string representation of customer object
    def __str__(self):
        return f"ID: {self.id} | Name: {self.first_name} {self.last_name}"

# Employee model
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    home_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    work_availability = models.BooleanField()
    hour_worked = models.IntegerField()
    # Custom string representation of employee object
    def __str__(self):
        return f"ID: {self.id} | Name: {self.first_name} {self.last_name}"

# DVD model
class Dvd(models.Model):
    title = models.CharField(max_length=200)
    actor = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    rent_price = models.DecimalField(max_digits = 4, decimal_places = 2)
    sell_price = models.DecimalField(max_digits = 4, decimal_places = 2)
    amount_instock = models.IntegerField()
    amount_bought = models.IntegerField()
    amount_sold = models.IntegerField()
    # Custom string representation of DVD object
    def __str__(self):
        return f"ID: {self.id} | Title: {self.title}"

# Request model
class Request(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    dvd_id = models.ForeignKey(Dvd, on_delete = models.CASCADE)

# Rental model
class Rental(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    dvd_id = models.ForeignKey(Dvd, on_delete = models.CASCADE)
    rent_date = models.DateField(auto_now = True)

# Special decorated function that decrement the DVD amount instock by 1 whenever an entry in the Rental table is created
@receiver(post_save, sender=Rental, dispatch_uid="decrement_stock_rental")
def decrement_stock_rental(sender, instance, **kwargs):
    instance.dvd_id.amount_instock -= 1
    instance.dvd_id.save()

# Special decorated function that increment the DVD amount instock by 1 whenever an entry in the Rental table is deleted
@receiver(post_delete, sender=Rental, dispatch_uid="increment_stock_return")
def increment_stock_return(sender, instance, **kwargs):
    instance.dvd_id.amount_instock += 1
    instance.dvd_id.save()

# To handle selling DVDs, we utilize the same decorated functions above but apply it to a table called sell
# Because there is no other easy way to implement logics to check and decrement amount instock
class Sell(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    dvd_id = models.ForeignKey(Dvd, on_delete = models.CASCADE)

# Special decorated function that decrement the DVD amount instock by 1 and increment amount sold by 1
# Whenever an entry in the Sell table is created
@receiver(post_save, sender=Sell, dispatch_uid="adjust_stock_sell")
def adjust_stock_sell(sender, instance, **kwargs):
    instance.dvd_id.amount_instock -= 1
    instance.dvd_id.amount_sold += 1
    instance.dvd_id.save()

