from django.contrib import admin
from .models import Content, Album, Parameter, Option, Product, Filter, ShowCase


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'small_text', 'big_text', 'button', 'link', 'type')
    list_filter = ('title', 'image', 'small_text', 'big_text', 'button', 'link', 'type')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'image')


class ParameterAdmin(admin.ModelAdmin):
    list_display = ['value']


class OptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_parameters')


class FilterAdmin(admin.ModelAdmin):
    list_display = ['by']


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('filter', 'flip', 'collection', 'customizable', 'publish')
    list_display = (
        'name', 'sku', 'image', 'options', 'filter', 'flip', 'collection', 'customizable',
        'sell_price', 'old_price', 'buy_price', 'publish', 'sell_ranking', 'client_ranking')


class ShowCaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'collection', 'position')


admin.site.register(Content, ContentAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Filter, FilterAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ShowCase, ShowCaseAdmin)
