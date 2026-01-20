from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth import logout as authlogout,login  as authlogin
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return HttpResponse('home page')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    return render(request,'authentication/register.html',{'form':form})

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            authlogin(request,user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request,'authentication/login.html',{'form':form})

def logout(request):
    authlogout(request)
    return redirect('register')

def profile(request):
    return render(request,'authentication/profile.html')

def redirecter(request):
    # print(request.user)
    return redirect('dashboard')
    # return HttpResponse('HOME PAGE')