from django.contrib import admin
from .models import Order, Destination


class OrderAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = (
        'order_ref', 'order_date', 'order_state', 'client_name', 'client_phone', 'registered_client', 'product_name',
        'product_color', 'product_option', 'product_shoe_size', 'product_clothing_size', 'product_price',
        'shipping_price', 'quantity',
        'shipping_destination', 'payment_method')
    list_filter = (
        'order_ref', 'order_date', 'order_state', 'client_name', 'client_phone', 'registered_client', 'product_name',
        'product_color', 'product_option', 'product_shoe_size', 'product_clothing_size', 'product_price',
        'shipping_price',
        'shipping_destination', 'payment_method')


class DestinationAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('name', 'standard_shipping', 'express_shipping')
    list_filter = ()


admin.site.register(Order, OrderAdmin)
admin.site.register(Destination, DestinationAdmin)
