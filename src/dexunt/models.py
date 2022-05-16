from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class ProductImage(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='dexunt/images/')

    def __str__(self):
        return self.name


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
    images = models.ManyToManyField(ProductImage, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    description = models.TextField(max_length=800)
    specification = models.TextField(max_length=800)
    catch_line = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rate = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.name


class Slide(models.Model):
    CHOICES = (
        ('FIRST', 'FIRST'),
        ('SECOND', 'SECOND'),
        ('THIRD', 'THIRD'),
    )
    image = models.ImageField(upload_to='dexunt/slides/')
    small_text = models.CharField(max_length=50, blank=True)
    big_text = models.CharField(max_length=50, blank=True)
    button = models.CharField(max_length=50, blank=True)
    link = models.URLField(blank=True, null=True)
    choice = models.CharField(max_length=50, choices=CHOICES, blank=True)

    def __str__(self):
        return self.small_text


class Banner(models.Model):
    CHOICES = (
        ('FIRST', 'FIRST'),
        ('SECOND', 'SECOND'),
        ('THIRD', 'THIRD'),
    )
    image = models.ImageField(upload_to='dexunt/banners/')
    small_text = models.CharField(max_length=50, blank=True)
    big_text = models.CharField(max_length=50, blank=True)
    button = models.CharField(max_length=50, blank=True)
    link = models.URLField(blank=True)
    choice = models.CharField(max_length=50, choices=CHOICES, blank=True)

    def __str__(self):
        return self.small_text
