from django.db import models
class Customer(models.Model):
    first_name = models.CharField(200)
    last_name = models.CharField(200)
    license_id = models.CharField(200)
    birth_date = models.DateField()
    home_address = models.CharField(200)
    phone_number = models.CharField(200)
    email_address = models.CharField(200)

class Employee(models.Model):
    username = models.CharField(200)
    password_hash = models.CharField(200)
    first_name = models.CharField(200)
    last_name = models.CharField(200)
    home_address = models.CharField(200)
    phone_number = models.CharField(200)
    work_availability = models.BooleanField()
    hour_worked = models.IntegerField()

class Dvd(models.Model):
    title = models.CharField(200)
    actor = models.CharField(200)
    director = models.CharField(200)
    genre = models.CharField(200)
    rent_price = models.DecimalField(4, 2)
    sell_price = models.DecimalField(4, 2) 
    amount_instock = models.IntegerField()
    amount_bought = models.IntegerField()
    amount_sold = models.IntegerField()

class Administrator(models.Model):
    username = models.CharField(200)
    password_hash = models.CharField(200)

class Credit_card(models.Model):
    card_number = models.CharField(200, primary_key = true)
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    first_name = models.CharField(200)
    last_name = models.CharField(200)
    expire_date = models.DateField()

class Rental(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    dvd_id = models.ForeignKey(Dvd, on_delete = models.CASCADE)
    rent_date = models.DateField(auto_now = true)

class Request(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    dvd_id = models.ForeignKey(Dvd, on_delete = models.CASCADE)