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
    type = models.CharField(max_length=50, choices=TYPES)

    class Meta:
        verbose_name_plural = "Content"

    def __str__(self):
        return self.title


class Album(models.Model):
    file_name = models.CharField(max_length=200, blank=True, default='product-image')
    image = models.ImageField(upload_to='store/images/')

    def __str__(self):
        return self.file_name


class Parameter(models.Model):
    value = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.value


class Option(models.Model):
    title = models.CharField(max_length=200, blank=True)
    parameter = models.ManyToManyField(Parameter, blank=True)

    def get_parameters(self):
        return "\n".join([p.value for p in self.parameter.all()])

    def __str__(self):
        return self.title


class Filter(models.Model):
    TYPES = (
        ('CATEGORY', 'CATEGORY'),
        ('TYPE', 'TYPE'),
        ('TAG', 'TAG'),
    )
    tag = models.CharField(max_length=200, blank=True, unique=True)
    type = models.CharField(max_length=50, choices=TYPES)

    def __str__(self):
        return self.tag


class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='store/products')
    album = models.ManyToManyField(Album, blank=True)
    option = models.ManyToManyField(Option, blank=True)
    category = models.ForeignKey('Filter', on_delete=models.CASCADE, related_name='filter_category')
    type = models.ForeignKey('Filter', on_delete=models.CASCADE, related_name='filter_type')
    tag = models.ForeignKey('Filter', on_delete=models.CASCADE, related_name='filter_tag')
    customizable = models.BooleanField(default=False)
    catch_line = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=800, blank=True)
    specification = models.TextField(max_length=800, blank=True)
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

    def get_options(self):
        return "\n".join([p.title for p in self.option.all()])

    def __str__(self):
        return self.name


class ShowCase(models.Model):
    TYPES = (
        ('SLIDE', 'SLIDE'),
        ('BANNER', 'BANNER'),
    )
    COLLECTION = (
        ('FLASH', 'FLASH'),
        ('SEASON', 'SEASON'),
        ('BOX', 'BOX'),
        ('LATEST', 'LATEST'),
        ('SELL', 'SELL'),
        ('RATE', 'RATE'),
    )
    title = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=50, choices=TYPES)
    collection = models.CharField(max_length=50, choices=COLLECTION, unique=True)
    position = models.IntegerField(default=1)

    def __str__(self):
        return self.title
