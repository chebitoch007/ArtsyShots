from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
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
    return render(request, 'register.html')

