from django.shortcuts import render

# home page

def home(request):
    return render(request,"pages/index.html")

def about(request):
    return render(request, "pages/about.html")

def services(request):
    return render(request, "pages/services.html")

def contact(request):
    return render(request, "pages/contact.html")