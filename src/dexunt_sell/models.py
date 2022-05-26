from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Destination(models.Model):
    name = models.CharField(max_length=200, unique=True)
    standard_shipping = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    express_shipping = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    code = models.CharField(max_length=200, unique=True)
    value = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class Order(models.Model):
    STATE = (
        ('REQUEST', 'REQUEST'),
        ('UNCONFIRMED', 'UNCONFIRMED'),
        ('CONFIRMED', 'CONFIRMED'),
        ('CANCELLED', 'CANCELLED'),
        ('DELIVERY', 'DELIVERY'),
        ('UNPAID', 'UNPAID'),
        ('PAYED', 'PAYED'),
        ('REJECTED', 'REJECTED'),
    )

    order_ref = models.CharField(max_length=200, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_state = models.CharField(max_length=50, choices=STATE, default='REQUEST')

    client_name = models.CharField(max_length=200, default='NOT-YET')
    client_phone = PhoneNumberField(blank=True)
    registered_client = models.BooleanField(default=False)

    coupon_value = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    coupon_code = models.CharField(max_length=200, default='UNDEFINED')

    product_sku = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200, default='UNDEFINED')
    product_color = models.CharField(max_length=200, default='UNDEFINED')
    product_option = models.CharField(max_length=200, default='UNDEFINED')
    product_shoe_size = models.CharField(max_length=200, default='UNDEFINED')
    product_clothing_size = models.CharField(max_length=200, default='UNDEFINED')
    product_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, default=1)

    shipping_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    shipping_destination = models.CharField(max_length=200, default='UNDEFINED')

    payment_method = models.CharField(max_length=50, default='CASH-ON-DELIVERY')
    cart_ref = models.CharField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.client_name
