from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from ArtsyShotsApp.models import Book


# Create your views here.
def about(request):
    return render(request, 'about.html')
def contact(request):
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


def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # Check if the user exists
        if user is not None:
            # login(request, user)
            login(request,user)
            messages.success(request, "You are now logged in!")
            return redirect('/home')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')





def hiring(request):
    return render(request, 'hiring.html')

def hiring(request):
    if request.method == "POST":
        myappointments = Book(
            name = request.POST['name'],
            email = request.POST['email'],
            phone_number = request.POST['phone_number'],
            message = request.POST['message'],
        )
        myappointments.save()
        return redirect('/hiring')

    else:
        return render(request, 'hiring.html')
