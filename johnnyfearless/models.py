# models.py
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
#from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your models here.
class User_data(models.Model):
    user_name = models.CharField(max_length=100)
    user_age = models.IntegerField()
    user_city = models.CharField(max_length=100)
    user_hobby = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

#class User_car(models.Model):
#    Car_name = models.CharField(max_length=100)
#    car_year = models.IntegerField()
#    car_model = models.CharField(max_length=100)
 
class products(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to="products/")
    product_cost = models.DecimalField(0, max_digits=10,decimal_places=2,default=0.00)
    product_manufacture_year = models.IntegerField()
    product_manufacturer = models.CharField(max_length=120,default="Unknown.")
    product_team = models.CharField(max_length=80, default="Toronto Blue Jays")
    product_extradetail = models.CharField(max_length=255,default="Product detail.")
    product_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product_name} {self.product_manufacture_year}"
    
def index(request):
    posts = products.all()  # fetching all post objects from database
    p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'product.html', context)
