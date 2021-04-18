from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    license_id = models.CharField(max_length=200)
    birth_date = models.DateField()
    home_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    def __str__(self):
        return f"ID: {self.id} | Name: {self.first_name} {self.last_name}"

class Employee(models.Model):
    username = models.CharField(max_length=200)
    password_hash = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    home_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    work_availability = models.BooleanField()
    hour_worked = models.IntegerField()
    def __str__(self):
        return f"ID: {self.id} | Name: {self.first_name} {self.last_name}"

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
    def __str__(self):
        return f"ID: {self.id} | Title: {self.title}"

class Administrator(models.Model):
    username = models.CharField(max_length=200)
    password_hash = models.CharField(max_length=200)

class CreditCard(models.Model):
    card_number = models.CharField(max_length=200, primary_key = True)
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    expire_date = models.DateField()

class Rental(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    dvd_id = models.ForeignKey(Dvd, on_delete = models.CASCADE)
    rent_date = models.DateField(auto_now = True)

class Request(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    dvd_id = models.ForeignKey(Dvd, on_delete = models.CASCADE)