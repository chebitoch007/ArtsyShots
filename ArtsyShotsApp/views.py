from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from ArtsyShotsApp.models import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import json




# Create your views here.
def about(request):
    return render(request, 'about.html')
def hiring(request):
    return render(request, 'hiring.html')
def gallery(request):
    return render(request, 'gallery.html')
def single(request):
    return render(request, 'gallery-single.html')
def index(request):
    return render(request, 'index.html')
def services(request):
    return render(request, 'services.html')
def starter(request):
    return render(request, 'starter-page.html')
def pay(request):
    return render(request, 'pay.html')
def register(request):
    return render(request, 'register.html')



def auth_page(request):
    return render(request, "register.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('/register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('/register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('/register')  # Redirect to login form

    return render(request, "register.html")



def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Set session expiry based on "Remember Me"
            if not remember_me:
                request.session.set_expiry(0)  # Session expires on browser close
            else:
                request.session.set_expiry(1209600)  # 2 weeks

            return redirect('home')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('/register')

    return render(request, "register.html")
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('/register')


@login_required
def home_view(request):
    return render(request, 'home.html')

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if not request.POST.get("remember_me"):
                request.session.set_expiry(0)  # Expire session on browser close
            return redirect("/home")  # Redirect to homepage
    else:
        form = AuthenticationForm()
    return render(request, "register.html",)












def book(request):
    if request.method == "POST":
        mybookings = book(
            name = request.POST['name'],
            email = request.POST['email'],
            phonenumber=request.POST['phone'],
            message=request.POST['message'],

        )
        mybookings.save()
        return redirect('/hiring')

    else:
        return render(request, 'hiring.html')

