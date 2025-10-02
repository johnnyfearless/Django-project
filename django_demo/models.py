# models.py
from django.db import models

# Create your models here.
class User_data(models.Model):
    user_name = models.CharField(max_length=100)
    user_age = models.IntegerField()
    user_city = models.CharField(max_length=100)
    user_hobby = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user_name)

class User_car(models.Model):
    Car_name = models.CharField(max_length=100)
    car_year = models.IntegerField()
    car_model = models.CharField(max_length=100)

class products(models.Model):
    product_name = models.CharField(max_length=200)
    product_cost = models.FloatField()
    product_manufacture_year = models.IntegerField()
    product_image = models.ImageField(upload_to="products/")
    product_available = models.BooleanField()

    def __str__(self):
        return str(self.product_name) + ", " + str(self.product_cost) + ", " + str(self.product_manufacture_year)

 
