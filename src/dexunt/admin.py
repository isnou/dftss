from django.contrib import admin
from .models import Item, ItemImage, Category, SubCategory, Slide, Banner, Option, Shoe, Clothing, Color, Shop, Brand


class ItemAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = (
        'id', 'name', 'sku', 'category', 'sub_category', 'brand', 'price', 'old_price', 'sell_rate', 'rate')
    list_filter = ('category', 'sub_category', 'brand', 'price', 'old_price', 'sell_rate', 'rate')


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
admin.site.register(Shop)
admin.site.register(Brand)
