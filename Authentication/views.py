from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth import logout as authlogout,login  as authlogin
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return HttpResponse('home page')


def register(request):
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
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            authlogin(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'authentication/login.html',{'form':form})

def logout(request):
    authlogout(request)
    return redirect('register')