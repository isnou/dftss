from django.contrib import admin
from .models import Content, Album, Product, ShowCase


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'small_text', 'big_text', 'button', 'link', 'type')
    list_filter = ('title', 'image', 'small_text', 'big_text', 'button', 'link', 'type')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'image')


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('tag', 'collection', 'publish')
    list_display = (
        'name', 'thumb', 'sku', 'tag', 'collection', 'publish_date', 'sell_price', 'old_price',
        'buy_price', 'quantity', 'publish', 'sell_ranking', 'client_ranking')


class ShowCaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'collection', 'position')


admin.site.register(Content, ContentAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ShowCase, ShowCaseAdmin)
