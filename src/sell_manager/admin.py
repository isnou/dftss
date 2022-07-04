from django.contrib import admin
from .models import Order, Item


class OrderAdmin(admin.ModelAdmin):
    list_display = ('ref', 'state', 'items', 'session_id', 'client_name', 'client_phone', 'registered_client',
                    'coupon_value', 'coupon_code', 'shipping_destination', 'shipping_price', 'total_price')


admin.site.register(Order, OrderAdmin)
