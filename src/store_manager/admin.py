from django.contrib import admin
from .models import Content, Album, Product, Filter, ShowCase


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'small_text', 'big_text', 'button', 'link', 'type')
    list_filter = ('title', 'image', 'small_text', 'big_text', 'button', 'link', 'type')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'image')


class FilterAdmin(admin.ModelAdmin):
    list_display = ['by']


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('filter', 'flip', 'collection', 'publish')
    list_display = (
        'name', 'thumb', 'sku', 'filter', 'flip', 'collection', 'type', 'publish_date', 'sell_price', 'old_price',
        'buy_price', 'quantity', 'publish', 'sell_ranking', 'client_ranking')


class ShowCaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'collection', 'position')


admin.site.register(Content, ContentAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Filter, FilterAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ShowCase, ShowCaseAdmin)
