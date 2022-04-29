from django.shortcuts import render
from .models import Team
from bikes.models import bike

# home page

def home(request):
    teams = Team.objects.all()
    feature_bike = bike.objects.filter(is_featured = True).order_by('-created_date')
    all_bikes = bike.objects.order_by('-created_date')
    context = {
        'teams':teams,
        'features':feature_bike,
        'all_bikes':all_bikes,
    }
    return render(request,"pages/index.html", context)

def about(request):
    teams = Team.objects.all()
    context = {
        'teams':teams,
    }
    return render(request, "pages/about.html", context)

def services(request):
    return render(request, "pages/services.html")

def contact(request):
    return render(request, "pages/contact.html")