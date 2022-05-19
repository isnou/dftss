from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class ItemImage(models.Model):
    album_name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='dexunt/images/')

    def __str__(self):
        return self.album_name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    @staticmethod
    def get_all_tags():
        return Tag.objects.all()

    def __str__(self):
        return self.name


class Shoe(models.Model):
    size = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.size


class Clothing(models.Model):
    size = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.size


class Color(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=300, unique=True)
    shoe_size = models.ManyToManyField(Shoe, blank=True, null=True)
    clothing_size = models.ManyToManyField(Clothing, blank=True, null=True)
    color = models.ManyToManyField(Color, blank=True, null=True)
    option = models.ManyToManyField(Option, blank=True, null=True)
    image = models.ImageField(upload_to='dexunt/slides/')
    images = models.ManyToManyField(ItemImage, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    description = models.TextField(max_length=800)
    specification = models.TextField(max_length=800)
    catch_line = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rate = models.IntegerField(
        default=5,
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
        return self.choice


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
        return self.choice
