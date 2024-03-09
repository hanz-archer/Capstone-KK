from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from django.views.decorators.cache import never_cache

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('base'))  # Use reverse to get the URL by name
        else:
            error = 'Invalid credentials. Please try again.'
            return render(request, 'KwentasApp/login.html', {'error': error})

    return render(request, 'KwentasApp/login.html')

@never_cache
@login_required
def base_view(request):
    print("Is authenticated:", request.user.is_authenticated)
    print("Session:", request.session)
    return render(request, 'KwentasApp/base.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Error creating account. Please check the form data.')
    else:
        form = RegistrationForm()

    return render(request, 'KwentasApp/register.html', {'form': form})

