from django.urls import path
from Cart import views


urlpatterns = [
    path('',views.cart_list,name='cart'),
    path('remove_from_cart/<int:id>/',views.remove_from_cart,name='remove_from_cart'),
    path('update_cart/<int:id>/',views.update_cart,name='update_cart'),
]
