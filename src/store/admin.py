from django.contrib import admin
from .models import Content, Album, Parameter, Option, Product, Collection, ShowCase


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'small_text', 'big_text', 'button', 'link', 'type')
    list_filter = ('title', 'image', 'small_text', 'big_text', 'button', 'link', 'type')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'image')


class ParameterAdmin(admin.ModelAdmin):
    list_display = ['value']


class OptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_parameters')


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'sku', 'image', 'get_albums', 'get_options', 'customizable', 'description', 'specification',
        'catch_line', 'sell_price', 'old_price', 'buy_price', 'publish', 'sell_ranking', 'client_ranking')


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'get_products', 'get_boxes')


class ShowCaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'location', 'collection')


admin.site.register(Content, ContentAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(ShowCase, ShowCaseAdmin)
