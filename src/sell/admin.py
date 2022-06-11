from django.contrib import admin
from .models import Order, Cart


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_ref', 'product_sku', 'product_name', 'product_color', 'product_option', 'product_size',
                    'product_price', 'quantity')


admin.site.register(Order, OrderAdmin)

