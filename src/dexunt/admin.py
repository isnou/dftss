from django.contrib import admin
from .models import Item, ItemImage, ProductImage, Category, Tag, Slide, Banner, Option

admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Slide)
admin.site.register(Banner)
admin.site.register(Option)


