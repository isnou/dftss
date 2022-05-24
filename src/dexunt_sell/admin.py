from django.contrib import admin
from .models import Order, Delivery, Destination, SubDestination


class OrderAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = (
        'order_ref', 'order_date', 'order_state', 'client_name', 'client_phone', 'registered_client', 'product_sku',
        'product_color', 'product_option', 'product_shoe_size', 'product_clothing_size', 'product_price',
        'delivery_price',
        'delivery_destination', 'payment_method')
    list_filter = (
        'order_ref', 'order_date', 'order_state', 'client_name', 'client_phone', 'registered_client', 'product_sku',
        'product_color', 'product_option', 'product_shoe_size', 'product_clothing_size', 'product_price',
        'delivery_price',
        'delivery_destination', 'payment_method')


class DeliveryAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('company_name', 'price')
    list_filter = ()


class DestinationAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('name', 'sub_destination', 'delivery_price')
    list_filter = ()


class SubDestinationAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('name')
    list_filter = ()


admin.site.register(Order, OrderAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(SubDestination, SubDestinationAdmin)

