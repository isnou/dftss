from django.db import models
from django.utils import timezone
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


class Album(models.Model):
    file_name = models.CharField(max_length=200, blank=True, default='product-image')
    image = models.ImageField(upload_to='store/images/')

    def __str__(self):
        return self.file_name


class Filter(models.Model):
    by = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.by


class Product(models.Model):
    COLLECTIONS = (
        ('FLASH', 'FLASH'),
        ('SEASON', 'SEASON'),
        ('BOX', 'BOX'),
    )
    TYPES = (
        ('INTRO', 'INTRO'),
        ('COLOR', 'COLOR'),
        ('SIZE', 'SIZE'),
        ('PACK', 'PACK'),
        ('OPTION', 'OPTION'),
    )
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200, unique=True, blank=True, null=True)
    image = models.ManyToManyField(Album, blank=True)
    filter = models.ForeignKey('Filter', on_delete=models.CASCADE, related_name='filter', blank=True, null=True)
    flip = models.ForeignKey('Filter', on_delete=models.CASCADE, related_name='flip', blank=True, null=True)
    collection = models.CharField(max_length=50, choices=COLLECTIONS, blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPES, blank=True, null=True)
    catch_line = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=800, blank=True)
    specification = models.TextField(max_length=800, blank=True)
    sell_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    buy_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    publish = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=timezone.now)
    sell_ranking = models.IntegerField(default=0)
    client_ranking = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def album(self):
        return "\n".join([p.file_name for p in self.image.all()])

    def __str__(self):
        return self.name


class Coupon(models.Model):
    code = models.CharField(max_length=200, unique=True)
    value = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class Destination(models.Model):
    name = models.CharField(max_length=200, unique=True)
    standard_shipping = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    express_shipping = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
