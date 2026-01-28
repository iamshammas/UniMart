from django.http import HttpResponse
from django.shortcuts import redirect, render

from Order.models import Order, OrderItem
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
    print("LOGIN VIEW HIT")
    if request.user.is_authenticated:
        print('User is authenticated')
        print(request.user)
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        print('POST request received')
        if form.is_valid():
            user = form.get_user()
            print('POST request received')
            print(user)
            authlogin(request,user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
        print('POST request received')
    print('POST request received')
    return render(request,'authentication/login.html',{'form':form})

def logout(request):
    authlogout(request)
    return redirect('register')

def profile(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request,'authentication/profile.html',{'orders':orders})

def redirecter(request):
    # print(request.user)
    return redirect('dashboard')
    # return HttpResponse('HOME PAGE')

def order_detail(request,order_id):
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request,'Order/order_detail.html',{'order':order, 'order_items': order_items})
    # return HttpResponse(f'Order Detail Page for Order ID: {order_id}')  

    # |mul:item.quantity 