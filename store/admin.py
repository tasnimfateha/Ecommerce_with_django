from django.contrib import admin
from .models.product import Products
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['title', 'price_detail_amount']




# Registering models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Customer)
admin.site.register(Order)

