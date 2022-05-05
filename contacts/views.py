from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

def inquiry(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        user_id = request.POST['user_id']
        bike_id = request.POST['bike_id']
        bike_title = request.POST['bike_title']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if request.user.is_authenticated:
            has_contact = Contact.objects.all().filter(user_id=user_id, bike_id=bike_id)
            if has_contact:
                messages.error(request, "You Inquiry was already submitted")
                return redirect('/bikes/'+bike_id)
        contact = Contact(first_name=first_name, last_name=last_name,customer_need=customer_need,bike_title=bike_title,user_id=user_id,
        bike_id=bike_id,city=city,state=state,email=email,phone=phone,message=message)
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                    'New inquiry on '+ bike_title,
                    'You have new inquiry on '+bike_title+'. Please login and check the admin panal for more information. http://127.0.0.1:8000/admin/contacts/contact/{}/change/'.format(bike_id),
                    'projectsalman4@gmail.com',
                    [admin_email],
                    fail_silently=False,
                )
        contact.save()
        messages.success(request, "You Inquiry is submitted")
        return redirect('/bikes/'+bike_id)


