from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def landing(request):
    return render(request, "landing.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
