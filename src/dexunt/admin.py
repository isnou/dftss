from django.contrib import admin
from .models import ProductImage, ProductSliderImage, ProductBannerImage, Category, Tag, Product

admin.site.register(ProductImage)
admin.site.register(ProductSliderImage)
admin.site.register(ProductBannerImage)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
