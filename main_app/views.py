from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from main_app.forms import LoginForm
from main_app.forms import CreateUserForm


# Create your views here.
def home(request):
    return render(request, 'index.html')


def service_details(request):
    return render(request, 'service-details.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def signin(request):
    if request.method == 'GET':

        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'signed in successfully')
                return redirect('home')
        messages.error(request, 'invalid username or password')
        return render(request, 'login.html', {'form': form})


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm()
        if form.is_valid():
            form.save()
            messages.success(request, 'signed up successfully')
    return render(request, 'signup.html', {'form': form})
