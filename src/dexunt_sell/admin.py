from django.contrib import admin
from .models import Order, Destination, Coupon


class OrderAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = (
        'order_ref', 'order_date', 'order_state', 'client_name', 'client_phone', 'registered_client', 'product_name',
        'product_color', 'product_option', 'product_shoe_size', 'product_clothing_size', 'quantity', 'product_price',
        'shipping_price', 'coupon_value', 'shipping_destination', 'payment_method')
    list_filter = (
        'order_ref', 'order_date', 'order_state', 'client_name', 'client_phone', 'registered_client', 'product_name',
        'shipping_destination')


class DestinationAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('name', 'standard_shipping', 'express_shipping')


class CouponAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('code', 'value', 'used')
    list_filter = ('value', 'used')


admin.site.register(Order, OrderAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Coupon, CouponAdmin)
