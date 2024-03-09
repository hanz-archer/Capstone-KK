from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib import messages

def login_view(request):
    return render(request, 'KwentasApp/login.html')

def base_view(request):
    return render(request, 'KwentasApp/base.html')


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

