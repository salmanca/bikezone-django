from ast import keyword
from django.shortcuts import get_object_or_404, render
from .models import Bike
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def bike(request):
    bikes = Bike.objects.order_by('-created_date')
    pagenation = Paginator(bikes, 2)
    page = request.GET.get('page')
    items = pagenation.get_page(page)
    model_search = Bike.objects.values_list('model', flat=True).distinct()
    year_search = Bike.objects.values_list('year', flat=True).distinct()
    location_search = Bike.objects.values_list('city', flat=True).distinct()
    color_search = Bike.objects.values_list('color', flat=True).distinct()
    context = {
        'features':items,
        'model_search':model_search,
        'year_search':year_search,
        'location_search':location_search,
        'color_search':color_search

    }
    return render(request, 'bikes/bikes.html', context)


def bike_details(request, id):
    single_bike = get_object_or_404(Bike, pk=id)
    context = {
        'bike':single_bike
    }
    return render(request, 'bikes/bike_details.html' , context)

def search(request):
    bikes = Bike.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            bikes = bikes.filter(description__icontains = keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            bikes = bikes.filter(model__iexact = model)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            bikes = bikes.filter(year__iexact = year)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            bikes = bikes.filter(city__iexact = city)

    if 'color' in request.GET:
        color = request.GET['color']
        if color:
            bikes = bikes.filter(color__iexact = color)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            bikes = bikes.filter(price__gte=min_price, price__lte = max_price)

    model_search = Bike.objects.values_list('model', flat=True).distinct()
    year_search = Bike.objects.values_list('year', flat=True).distinct()
    location_search = Bike.objects.values_list('city', flat=True).distinct()
    color_search = Bike.objects.values_list('color', flat=True).distinct()
    context = {
        'bikes':bikes,
        'model_search':model_search,
        'year_search':year_search,
        'location_search':location_search,
        'color_search':color_search

    }
    return render(request, 'bikes/search.html', context)