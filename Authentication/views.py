from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth import logout as authlogout

# Create your views here.

def home(request):
    return HttpResponse('home page')


def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request,'authentication/register.html',{'form':form})

def login(request):
    return HttpResponse('login page')

def logout(request):
    authlogout(request)
    return redirect('register')