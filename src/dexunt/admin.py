from django.contrib import admin
from .models import Item, ItemImage, Category, SubCategory, \
    Slide, Banner, Option, Shoe, Clothing, Color, Shop, Brand, ShoppingCart, Order


class ItemAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('id', 'name', 'sku', 'category', 'sub_category', 'brand', 'price', 'old_price', 'sell_rate', 'rate')
    list_filter = ('category', 'sub_category', 'brand', 'price', 'old_price', 'sell_rate', 'rate')


class ShopAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('id', 'name')
    list_filter = ('category', 'sub_category', 'shoe_size', 'clothing_size', 'color', 'option', 'brand')


class OrderAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('client_name', 'client_phone', 'product_name', 'quantity', 'coupon', 'delivery', 'shoe_size',
                    'clothing_size', 'color', 'option', 'city', 'town', 'client_raw_phone')
    list_filter = ('client_name', 'client_phone', 'product_name', 'city', 'town')


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Slide)
admin.site.register(Banner)
admin.site.register(Option)
admin.site.register(Shoe)
admin.site.register(Clothing)
admin.site.register(Color)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Brand)
admin.site.register(ShoppingCart)
admin.site.register(Order)

# , 'product', 'category', 'sub_category', 'shoe_size', 'clothing_size', 'color', 'option', 'brand'


#  'name', 'phone', 'email', 'product', 'quantity', 'color', 'option', 'size', 'created_at', 'updated_at'



