from django.contrib import admin
from .models import Order, Shipping, Destination, SubDestination


class OrderAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = (
        'order_ref', 'order_date', 'order_state', 'client_name', 'client_phone', 'registered_client', 'product_sku',
        'product_color', 'product_option', 'product_shoe_size', 'product_clothing_size', 'product_price',
        'shipping_price',
        'shipping_destination', 'payment_method')
    list_filter = (
        'order_ref', 'order_date', 'order_state', 'client_name', 'client_phone', 'registered_client', 'product_sku',
        'product_color', 'product_option', 'product_shoe_size', 'product_clothing_size', 'product_price',
        'shipping_price',
        'shipping_destination', 'payment_method')


class ShippingAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('choice', 'price')
    list_filter = ()


class DestinationAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('name', 'shipping', 'get_sub_destination')
    list_filter = ()


class SubDestinationAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ['name']
    list_filter = ()


admin.site.register(Order, OrderAdmin)
admin.site.register(Shipping, ShippingAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(SubDestination, SubDestinationAdmin)

