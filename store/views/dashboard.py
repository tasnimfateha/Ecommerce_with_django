from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware




def user_dashboard(request):
    customer = Customer.objects.get(id=request.session['customer'])
    
    orders = Order.get_orders_by_customer(customer.id)
    context = {'customer': customer, 'orders': orders}
    
    return render(request, 'user_dashboard.html', context)



def admin_dashboard(request):
    if request.session.get('customer'):  # check if customer is logged in
        customer_id = request.session['customer']
        customer = Customer.objects.get(id=customer_id)
        if customer.is_superuser:
            return render(request, 'admin_dashboard.html')
    return redirect('login')

