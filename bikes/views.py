from django.shortcuts import render

# Create your views here.
def bike(request):
    return render(request, 'bikes/bikes.html')