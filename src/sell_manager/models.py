from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Item(models.Model):
    sku = models.CharField(max_length=200)
    name = models.CharField(max_length=200, default='UNDEFINED')
    thumb = models.ImageField(upload_to='store-manager/products', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, default=1)

    def __str__(self):
        return self.sku


class Order(models.Model):
    STATE = (
        ('REQUEST', 'REQUEST'),
        ('UNCONFIRMED', 'UNCONFIRMED'),
        ('CONFIRMED', 'CONFIRMED'),
        ('PEND', 'PEND'),
        ('CANCELLED', 'CANCELLED'),
        ('REMOVED', 'REMOVED'),
        ('DELIVERY', 'DELIVERY'),
        ('UNPAID', 'UNPAID'),
        ('PAYED', 'PAYED'),
        ('REJECTED', 'REJECTED'),
    )
    ref = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=50, choices=STATE, default='REQUEST')
    item = models.ManyToManyField(Item, blank=True)
    session_id = models.CharField(max_length=200, unique=True, null=True)
    client_name = models.CharField(max_length=200, default='UNDEFINED')
    client_phone = PhoneNumberField(blank=True)
    registered_client = models.BooleanField(default=False)
    coupon_value = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    coupon_code = models.CharField(max_length=200, default='UNDEFINED')
    shipping_destination = models.CharField(max_length=200, default='UNDEFINED')
    shipping_sub_destination = models.CharField(max_length=200, default='UNDEFINED')
    shipping_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def items(self):
        return "\n".join([p.name for p in self.item.all()])

    def items_count(self):
        return self.item.all().count()

    def __str__(self):
        return self.ref
