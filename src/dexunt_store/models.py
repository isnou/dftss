from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class Album(models.Model):
    name = models.CharField(max_length=200, blank=True, default='item-image')
    image = models.ImageField(upload_to='dexunt_store/images/')

    def __str__(self):
        return self.name


class Category(models.Model):
    code = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='dexunt_store/images/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.slug


class SubCategory(models.Model):
    code = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='dexunt_store/images/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "SubCategories"

    def __str__(self):
        return self.slug


class Tag(models.Model):
    code = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='dexunt_store/images/', blank=True, null=True)

    def __str__(self):
        return self.slug


class Brand(models.Model):
    code = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='dexunt_store/images/', blank=True, null=True)

    def __str__(self):
        return self.slug


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


class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200, unique=True)
    shoe_size = models.ManyToManyField(Shoe, blank=True)
    clothing_size = models.ManyToManyField(Clothing, blank=True)
    color = models.ManyToManyField(Color, blank=True)
    option = models.ManyToManyField(Option, blank=True)
    image = models.ImageField(upload_to='dexunt_sotre/products')
    images = models.ManyToManyField(Album, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=800)
    specification = models.TextField(max_length=800)
    catch_line = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sell_rate = models.IntegerField(default=0)
    rate = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.name


class Content(models.Model):
    CHOICES = (
        ('FIRST-SLIDE', 'FIRST-SLIDE'),
        ('SECOND-SLIDE', 'SECOND-SLIDE'),
        ('THIRD-SLIDE', 'THIRD-SLIDE'),
        ('FIRST-BANNER', 'FIRST-BANNER'),
        ('SECOND-BANNER', 'SECOND-BANNER'),
        ('THIRD-BANNER', 'THIRD-BANNER'),
    )
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='dexunt_sotre/content')
    small_text = models.CharField(max_length=50, blank=True)
    big_text = models.CharField(max_length=50, blank=True)
    button = models.CharField(max_length=50, blank=True)
    link = models.URLField(blank=True)
    choice = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name_plural = "Content"

    def __str__(self):
        return self.choice


class ShowCase(models.Model):
    CHOICES = (
        ('SLIDE', 'SLIDE'),
        ('BANNER', 'BANNER'),
    )
    name = models.CharField(max_length=200, unique=True)
    product = models.ManyToManyField(Product)
    category = models.ManyToManyField(Category, blank=True)
    sub_category = models.ManyToManyField(SubCategory, blank=True)
    shoe_size = models.ManyToManyField(Shoe, blank=True)
    clothing_size = models.ManyToManyField(Clothing, blank=True)
    color = models.ManyToManyField(Color, blank=True)
    option = models.ManyToManyField(Option, blank=True)
    brand = models.ManyToManyField(Brand, blank=True)
    choice = models.CharField(max_length=50, choices=CHOICES)

    def get_product(self):
        return "\n".join([p.name for p in self.product.all()])

    def get_category(self):
        return "\n".join([p.slug for p in self.category.all()])

    def get_sub_category(self):
        return "\n".join([p.slug for p in self.sub_category.all()])

    def get_shoe_size(self):
        return "\n".join([p.size for p in self.shoe_size.all()])

    def get_clothing_size(self):
        return "\n".join([p.size for p in self.clothing_size.all()])

    def get_color(self):
        return "\n".join([p.name for p in self.color.all()])

    def get_option(self):
        return "\n".join([p.name for p in self.option.all()])

    def get_brand(self):
        return "\n".join([p.slug for p in self.brand.all()])

    def __str__(self):
        return self.name
