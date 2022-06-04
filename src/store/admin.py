from django.contrib import admin
from .models import Content, Album, Size, Color, Pack, Brand, Package, Product, Box, Collection, ShowCase


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'small_text', 'big_text', 'button', 'link', 'type')
    list_filter = ('title', 'image', 'small_text', 'big_text', 'button', 'link', 'type')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'image')


class SizeAdmin(admin.ModelAdmin):
    list_display = ('type', 'value')


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name')


class PackAdmin(admin.ModelAdmin):
    list_display = ('name')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')


class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'image', 'album', 'pack', 'description', 'customizable')


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'sku', 'image', 'album', 'size', 'color', 'pack', 'customizable', 'brand', 'description',
        'specification',
        'catch_line', 'sell_price', 'old_price', 'buy_price', 'publish', 'sell_ranking', 'client_ranking')


class BoxAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'product', 'package', 'customizable', 'brand', 'description', 'specification', 'catch_line',
        'sell_price',
        'old_price', 'buy_price', 'publish', 'sell_ranking', 'client_ranking')


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'product', 'box')


class ShowCaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'location', 'collection')


admin.site.register(Content, ContentAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Pack, PackAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Box, BoxAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(ShowCase, ShowCaseAdmin)
