from functools import reduce
from django.contrib.auth import decorators
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout  
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import CreateUserForm




def registerPage(request): #sign_up view generates our form with empty information or the request//post data if there is any
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm(request.POST)
        if request.method == "POST":
            if form.is_valid():  #verifies if the two password  are same which tehn calls set_passwords() to hash and save our password into the database
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was creater for " + user)

                return redirect('login')


        context = {'form' : form }
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username= username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else: 
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'accounts/login.html',context)



@login_required(login_url='login')
def home(request):
    return render(request,'accounts/main.html')


def logoutPage(request):
    logout(request)
    return redirect('login')