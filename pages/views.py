from django.shortcuts import render
from .models import Team
from bikes.models import Bike

# home page

def home(request):
    teams = Team.objects.all()
    feature_bike = Bike.objects.filter(is_featured = True).order_by('-created_date')
    all_bikes = Bike.objects.order_by('-created_date')
    model_search = Bike.objects.values_list('model', flat=True).distinct()
    year_search = Bike.objects.values_list('year', flat=True).distinct()
    location_search = Bike.objects.values_list('city', flat=True).distinct()
    color_search = Bike.objects.values_list('color', flat=True).distinct()
    context = {
        'teams':teams,
        'features':feature_bike,
        'all_bikes':all_bikes,
        'model_search':model_search,
        'year_search':year_search,
        'location_search':location_search,
        'color_search':color_search

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