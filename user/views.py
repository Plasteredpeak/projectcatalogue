from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from .forms import SignupForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('/projects')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'user/signup.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('/')