
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

# Create your views here.

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from .forms import RegisterForm

def home(request):

    return render(
        request,
        'home.html'
    )

def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            if user.role == 'candidate':
                return redirect('/candidate-dashboard/')

            elif user.role == 'recruiter':
                return redirect('/recruiter-dashboard/')

            elif user.role == 'admin':
                return redirect('/admin-dashboard/')

    return render(
        request,
        'accounts/login.html'
    )

def logout_view(request):

    logout(request)

    return redirect('login')