from django.contrib import admin
from django.urls import path
from .views.home import Index , store, product_search
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.dashboard import user_dashboard, admin_dashboard
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('product_search', product_search, name='product_search'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('user_dashboard', user_dashboard, name='user_dashboard'),
    path('admin_dashboard', admin_dashboard, name='admin_dashboard'),

]