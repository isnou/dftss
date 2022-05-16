from django.contrib import admin
from .models import ProductImage, Category, Tag, Product

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Tag)


