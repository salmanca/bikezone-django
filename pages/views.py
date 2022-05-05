from django.shortcuts import render,redirect
from .models import Team
from bikes.models import Bike
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        email_subject = 'You have new message from '+name+ '. The Message subject is '+ subject
        email_body = 'Name: '+ name + '.\nEmail: '+ email +'.\nPhone: '+ phone + '.\nMessage: '+ message
        send_mail(
                email_subject,
                email_body,
                'projectsalman4@gmail.com',
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, "You Message is sended successfully. We will get back to you")
        return redirect('contact')

    return render(request, "pages/contact.html")