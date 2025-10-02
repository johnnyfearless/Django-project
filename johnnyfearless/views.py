# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from johnnyfearless.models import products
from johnnyfearless.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
#from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger#from .models import Post  # Importing your Post model
from .forms import CustomUserCreationForm

#@login_required
def home_page(request):
    the_return_data = {
        'home_last':"Testing"
        }
    
    return render(request, 'home.html', the_return_data)

#@login_required
def contact_page(request):
    return render(request, 'contact.html')

#@login_required
def form_page(request):
    if request.method == "POST":
        usr_name = request.POST["u_name"]
        usr_age = request.POST["u_age"]
        usr_city = request.POST["u_city"]
        usr_hobby = request.POST["u_hobby"]

        user_data_model = User_data(user_name = usr_name,
                                    user_age = usr_age,
                                    user_city =  usr_city,
                                    user_hobby = usr_hobby)
        user_data_model.save()

    return render(request, 'form.html')

#@login_required
def user_list(request):
    users_list = User_data.objects.all()
    return_data = {"Users_list" : list(users_list)}
    return render(request, 'user_list.html', return_data)

#@login_required
def user_update(request, user_id):
    if request.method == "POST":
        users_list = User_data.objects.filter(id = user_id)
        user_date_update = users_list[0]
        user_date_update.user_name = request.POST["u_name"]
        user_date_update.user_age = request.POST["u_age"]
        user_date_update.user_city = request.POST["u_city"]
        user_date_update.user_hobby = request.POST["u_hobby"]
        user_date_update.save()
        return redirect("user_list_path")
    else:
        users_list = User_data.objects.filter(id = user_id).values()
        user_date_return = list(users_list)[0]
        return render(request, 'user_update.html', user_date_return)

#login_required 
def user_delete(request, user_id):
    users_list = User_data.objects.filter(id = user_id)
    user_date_update = users_list[0]
    user_date_update.delete()
    return redirect("user_list_path")

#@login_required
def product_list(request):
    pro_list = products.objects.filter(product_available = True)
    product_data = {'product_list': list(pro_list)}
    return render(request, 'product.html', product_data)

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Login Success")
            return redirect("home_page_path")
        else:
            messages.error(request,"Invalid credentials, Please check and login again")
    return render(request, "login.html")

#def user_signup(request):
#    if request.method == "POST":
#        username = request.POST["username"]
#        password = request.POST["password"]
#        user = authenticate(request, username=username, password=password)
#        if user is not None:
#            signup(request, user)
#            messages.success(request,"Login Success")
#            return redirect("home_page_path")
#        else:
#            messages.error(request,"Invalid credentials, Please check and login again")
#    return render(request, "signup.html")
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
 
@login_required
def profile(request):
    return render(request, 'user_update.html')

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(product_list, 5)  # Show 5 posts per page

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {'page_obj': page_obj}
    return render(request, 'product.html', context)