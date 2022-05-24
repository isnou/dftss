from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('order_ref', 'order_date', 'order_state', 'client_name', 'client_phone', 'registered_client', 'product_sku', 'product_color', 'product_option', 'product_shoe_size', 'product_clothing_size', 'product_price', 'delivery_price', 'delivery_destination', 'payment_method')
    list_filter = ('order_ref', 'order_date', 'order_state', 'client_name', 'client_phone', 'registered_client', 'product_sku', 'product_color', 'product_option', 'product_shoe_size', 'product_clothing_size', 'product_price', 'delivery_price', 'delivery_destination', 'payment_method')


admin.site.register(Order, OrderAdmin)

# , 'product', 'category', 'sub_category', 'shoe_size', 'clothing_size', 'color', 'option', 'brand'


#  'name', 'phone', 'email', 'product', 'quantity', 'color', 'option', 'size', 'created_at', 'updated_at'
