from django.contrib import admin
from .models import Product, Album, Category, SubCategory, Tag, Brand, Shoe, Clothing, Color, Option, Content, ShowCase


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'sku', 'category', 'sub_category',
                    'brand', 'price', 'old_price', 'sell_rate', 'rate',
                    'publish_rate', 'collection', 'publish')
    list_filter = ('category', 'sub_category', 'brand', 'price',
                   'publish_rate', 'sell_rate', 'rate', 'collection',
                   'publish')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'slug', 'image')


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'slug', 'image')


class TagAdmin(admin.ModelAdmin):
    list_display = ('code', 'slug', 'image')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('code', 'slug', 'image')


class ContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'small_text',
                    'big_text', 'button', 'link', 'choice')


class ShowCaseAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'choice', 'collection')


admin.site.register(Product, ProductAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Shoe)
admin.site.register(Clothing)
admin.site.register(Color)
admin.site.register(Option)
admin.site.register(Content, ContentAdmin)
admin.site.register(ShowCase, ShowCaseAdmin)
