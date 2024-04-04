from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

from .models import User


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)
                        
                return redirect('/')

    return render(request, 'user/login.html')


def signup(request):
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        if name and email and password and password2:
            user = User.objects.create_user(name, email, password)

            print('User created:', user)

            return redirect('/login/')
        else:
            print('Something went wrong')
    else:
        return render(request, 'user/signup.html')

    return render(request, 'user/signup.html')