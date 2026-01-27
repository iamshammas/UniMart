from django.http import HttpResponse
from django.shortcuts import redirect, render
from Cart.models import Cart
from .models import Order, OrderItem
from Authentication.models import Profile
# Create your views here.


def checkout(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')
        total_amount = Cart.objects.get(id=request.user.id).total_amount
        profile = Profile.objects.get(user=request.user)
        profile.name = name
        profile.phone = phone
        profile.address = address
        profile.save()
        order = Order.objects.create(
            user=user,
            payment_method=payment_method,
            total_amount=total_amount
        )
        if order:
            order.save()
        cart_items = Cart.objects.get(id=request.user.id).items.all()

        order_items=[]
        for item in cart_items:
            order_items.append(
                OrderItem(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
            )
        OrderItem.objects.bulk_create(order_items)
        return redirect('place_order')
    cart = Cart.objects.get(id=request.user.id)
    cart_items = cart.items.all()
    cart_tot = cart.total_amount
    context  = {
        'cart_items':cart_items,
        'cart_tot':cart_tot,
        'cart':cart
    }
    return render(request,'Order/checkout.html',context)

def place_order(request):
    return HttpResponse('Hello Place order page')

def orders(request):
    return HttpResponse('Hello orders page')