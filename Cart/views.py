from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import CartItem

# Create your views here.

def cart_list(request):
    cart_items = CartItem.objects.filter(cart__user=request.user.id)
    # total_amount = CartItem.objects.filter(cart__user=request.user.id).aggregate(sum("produc"))
    sum=0
    return render(request, 'cart/cart.html',{'cart_items':cart_items})


def remove_from_cart(request,id):
    prod = get_object_or_404(CartItem,id=id)
    prod.delete()
    return redirect('cart')

def update_cart(request,id):
    prod = get_object_or_404(CartItem,id=id)
    if request.method == 'POST':
        prod.quantity = request.POST.get('quantity')
        prod.save()
    return redirect('cart')