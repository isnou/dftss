from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    order_ref = models.CharField(max_length=200, unique=True)
    product_sku = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200, default='UNDEFINED')
    product_image = models.ImageField(upload_to='dexunt-sotre/products', blank=True)
    product_color = models.CharField(max_length=200, default='UNDEFINED')
    product_option = models.CharField(max_length=200, default='UNDEFINED')
    product_size = models.CharField(max_length=200, default='UNDEFINED')
    product_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, default=1)

    def __str__(self):
        return self.product_name


class Cart(models.Model):
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
    cart_ref = models.CharField(max_length=200, unique=True)
    cart_date = models.DateTimeField(auto_now_add=True)
    cart_state = models.CharField(max_length=50, choices=STATE, default='REQUEST')
    order = models.ManyToManyField(Order, blank=True)
    client_name = models.CharField(max_length=200, default='UNDEFINED')
    client_phone = PhoneNumberField(blank=True)
    registered_client = models.BooleanField(default=False)
    coupon_value = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    coupon_code = models.CharField(max_length=200, default='UNDEFINED')
    shipping_destination = models.CharField(max_length=200, default='UNDEFINED')
    shipping_sub_destination = models.CharField(max_length=200, default='UNDEFINED')
    shipping_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def orders(self):
        return "\n".join([p.product_name for p in self.order.all()])

    def orders_count(self):
        return self.order.all().count()

    def __str__(self):
        return self.cart_ref
