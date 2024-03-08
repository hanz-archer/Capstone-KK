from django.shortcuts import render

def login_view(request):
    return render(request, 'KwentasApp/login.html')

def base_view(request):
    return render(request, 'KwentasApp/base.html')
