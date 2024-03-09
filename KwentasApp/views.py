from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def login_view(request):
    return render(request, 'KwentasApp/login.html')

def base_view(request):
    return render(request, 'KwentasApp/base.html')

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base') 
    else:
        form = UserCreationForm()

    return render(request, 'KwentasApp/register.html', {'form': form})