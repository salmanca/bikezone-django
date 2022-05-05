from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credetials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                    user.save()
                    auth.login(request, user)
                    messages.success(request, 'loged in successfully')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Email already exists')
                    return redirect('register')
            else:
                messages.error(request, 'Username already exists')
                return redirect('register')
        else:
            messages.error(request, 'Password does not match')
            return redirect('register')
    return render(request, 'accounts/register.html')

@login_required(login_url = 'login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by("-created_date").filter(user_id = request.user.id)
    context = {
        "user_inquiry":user_inquiry
    }
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('login')