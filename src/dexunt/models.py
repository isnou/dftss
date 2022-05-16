from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class ProductImage(models.Model):
    image = models.ImageField(upload_to='dexunt/images/')

    def __str__(self):
        return self.image


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=300, unique=True)
    main_image = models.ImageField(upload_to='dexunt/main/image/', blank=True)
    slider_image = models.ImageField(upload_to='dexunt/slider/image/', blank=True)
    images = models.ManyToManyField(ProductImage, blank=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag',on_delete=models.CASCADE)
    description = models.TextField(max_length=800)
    specification = models.TextField(max_length=800)
    catch_line = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rate = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.name
