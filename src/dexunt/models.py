from django.db import models, IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class ProductImage(models.Model):
    link = models.ImageField(upload_to='dexunt/picture/image/')

    def __str__(self):
        return self.link.url


class ProductBannerImage(models.Model):
    link = models.ImageField(upload_to='dexunt/banner-picture/image/')

    def __str__(self):
        return self.link.url


class ProductSliderImage(models.Model):
    link = models.ImageField(upload_to='dexunt/slider-picture/image/')

    def __str__(self):
        return self.link.url


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=300)
    product_image = models.ManyToManyField(ProductImage, blank=True, related_name="product_img")
    product_banner_image = models.ManyToManyField(ProductBannerImage, blank=True, related_name="product_banner_img")
    product_slider_image = models.ManyToManyField(ProductSliderImage, blank=True, related_name="product_slider_img")
    category = models.ForeignKey(Category)
    tag = models.ForeignKey(Tag)
    description = models.TextField(max_length=800)
    specification = models.TextField(max_length=800)
    catch_line = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8)
    rate = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.name
