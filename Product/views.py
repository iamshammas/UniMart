from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Product,Category
from Cart.models import Cart,CartItem

# Create your views here.

@login_required
def dashboard(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    data = {
        'products' : products,
        'categories' : categories
    }
    return render(request,'product/product_list.html',data)


@login_required
def product_detail(request,slug):
    obj = get_object_or_404(Product,slug=slug)
    return render(request,'product/product_detail.html',{'product':obj})

@login_required
def category_products(request,slug):
    products = Product.objects.filter(Category__slug=slug)
    categories = Category.objects.all()
    print('HELLOOOOOOOOOOOOOOI')
    data = {
        'products' : products,
        'categories' : categories
    }
    return render(request,'product/product_list.html',data)

from django.contrib.auth.models import User
def add_to_cart(request,id):
    product = get_object_or_404(Product, id=id)
    userr = request.user
    # cart = get_object_or_404(Cart,user=userr )
    cart,created = Cart.objects.get_or_create(user=userr)
    # user = User.objects.get(username='admin')
    # print(request.user)
    CartItem.objects.create(cart=cart,product=product,quantity=1)
    return redirect('cart')