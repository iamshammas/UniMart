from . import views
from django.urls import path,include


urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='loginn'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('prod/',include('Product.urls'),name='prod'),
    path('order/<int:order_id>/',views.order_detail,name='order_detail'),
]
