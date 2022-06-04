from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Content(models.Model):
    TYPES = (
        ('FIRST-TYPE', 'FIRST-TYPE'),
        ('SECOND-TYPE', 'SECOND-TYPE'),
        ('THIRD-TYPE', 'THIRD-TYPE'),
    )
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='store/content')
    small_text = models.CharField(max_length=50, blank=True)
    big_text = models.CharField(max_length=50, blank=True)
    button = models.CharField(max_length=50, blank=True)
    link = models.URLField(blank=True)
    type = models.CharField(max_length=50, choices=TYPES, unique=True)

    class Meta:
        verbose_name_plural = "Content"

    def __str__(self):
        return self.title


class Album(models.Model):
    file_name = models.CharField(max_length=200, blank=True, default='product-image')
    image = models.ImageField(upload_to='store/images/')

    def __str__(self):
        return self.file_name


class Size(models.Model):
    type = models.CharField(max_length=200, blank=True)
    value = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.value


class Color(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Pack(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='store/brands/', blank=True, null=True)

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=200, unique=True)
    sku = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='store/packages')
    album = models.ManyToManyField(Album, blank=True)
    pack = models.ManyToManyField(Pack, blank=True)
    description = models.TextField(max_length=800, blank=True)
    customizable = models.BooleanField(default=False)

    def get_albums(self):
        return "\n".join([p.file_name for p in self.album.all()])

    def get_packs(self):
        return "\n".join([p.name for p in self.pack.all()])

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='store/products')
    album = models.ManyToManyField(Album, blank=True)
    size = models.ManyToManyField(Size, blank=True)
    color = models.ManyToManyField(Color, blank=True)
    pack = models.ManyToManyField(Pack, blank=True)
    customizable = models.BooleanField(default=False)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, blank=True)
    description = models.TextField(max_length=800, blank=True)
    specification = models.TextField(max_length=800, blank=True)
    catch_line = models.CharField(max_length=200, blank=True)
    sell_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    buy_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    publish = models.BooleanField(default=True)
    sell_ranking = models.IntegerField(default=0)
    client_ranking = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def get_albums(self):
        return "\n".join([p.file_name for p in self.album.all()])

    def get_sizes(self):
        return "\n".join([p.value for p in self.size.all()])

    def get_colors(self):
        return "\n".join([p.name for p in self.color.all()])

    def get_packs(self):
        return "\n".join([p.name for p in self.pack.all()])

    def __str__(self):
        return self.name


class Box(models.Model):
    name = models.CharField(max_length=200)
    product = models.ManyToManyField(Product, blank=True)
    package = models.ManyToManyField(Package, blank=True)
    customizable = models.BooleanField(default=False)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, blank=True)
    description = models.TextField(max_length=800, blank=True)
    specification = models.TextField(max_length=800, blank=True)
    catch_line = models.CharField(max_length=200, blank=True)
    sell_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    buy_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    publish = models.BooleanField(default=True)
    sell_ranking = models.IntegerField(default=0)
    client_ranking = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def get_products(self):
        return "\n".join([p.name for p in self.product.all()])

    def get_packages(self):
        return "\n".join([p.name for p in self.package.all()])

    class Meta:
        verbose_name_plural = "Boxes"

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=200)
    product = models.ManyToManyField(Product, blank=True)
    box = models.ManyToManyField(Box, blank=True)

    def get_products(self):
        return "\n".join([p.name for p in self.product.all()])

    def get_boxes(self):
        return "\n".join([p.name for p in self.box.all()])

    def __str__(self):
        return self.name


class ShowCase(models.Model):
    TYPES = (
        ('SLIDE', 'SLIDE'),
        ('BANNER', 'BANNER'),
    )
    name = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=50, choices=TYPES)
    location = models.IntegerField(default=1)
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name
