from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="authentication/login.html"),
        name="login",
    ),
    path('',views.dashboard,name='dashboard'),
    path('ffdf/<slug:slug>/',views.product_detail,name='product_detail'),
    path('category/<slug:slug>/',views.category_products,name='category_products'),
    path('cart/',include('Cart.urls'),name='show_cart'),
    path('cart/add/<int:id>/',views.add_to_cart,name='add_to_cart'),
]
