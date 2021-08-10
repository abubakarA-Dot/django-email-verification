from django.shortcuts import render, redirect
from .forms import CreateUserForm
from .models import Users
from django.contrib import messages
import uuid

# Create your views here.

def home_view(request):
    context = {
        'home': 'Home View'
    }
    return render(request, 'base.html', context)

def sign_up(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            # messages.SUCCESS(request, "Your profile is created.")
            return redirect('login')
            # user_info = form.save(commit=False)
            # user_prof = Users.objects.create(email= email, verification_token=str(uuid.uuid4))
            
    context = {'signup':form}
    return render(request, 'signup.html', context)

'''
try:
            if Users.objects.filter(email = email).first():
                messages.WARNING(request, "User with this email already exists")
                return redirect('sign-up')
            user_profile = Users.objects.create(
                email=email, password=password, verification_token=str(uuid.uuid4))
            user_profile.save()
            return redirect('sent_token')
        except Exception as e:
            print('Exception error', e)
            return e
'''


def login(request):
    context = {}
    return render(request, 'login.html', context)

def token_sent(request):
    return render(request, 'send_token.html')
