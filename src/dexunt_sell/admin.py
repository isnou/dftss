from django.contrib import admin
from .models import Order, Destination, Coupon, GroupOrder


class OrderAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('order_ref', 'product_name', 'product_color', 'product_option', 'product_shoe_size',
                    'product_clothing_size', 'quantity', 'product_price', 'product_image')
    list_filter = ('order_ref', 'product_name')


class GroupOrderAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('group_order_ref', 'group_order_date', 'group_order_state', 'get_orders', 'client_name',
                    'client_phone', 'registered_client', 'coupon_value', 'coupon_code', 'total_price', 'shipping_price',
                    'shipping_destination', 'shipping_sub_destination', 'request', 'registered_client')
    list_filter = ('group_order_ref', 'group_order_date', 'group_order_state')


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
admin.site.register(GroupOrder, GroupOrderAdmin)
