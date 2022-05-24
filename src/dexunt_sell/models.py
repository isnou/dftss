from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class SubDestination(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    company_name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name_plural = "Delivery"

    def __str__(self):
        return self.company_name


class Destination(models.Model):
    name = models.CharField(max_length=200, unique=True)
    sub_destination = models.ManyToManyField(SubDestination, blank=True)
    delivery_price = models.ManyToManyField(Delivery, blank=True)

    def get_delivery_prices(self):
        return "\n".join([p.delivery_prices for p in self.delivery_price.all()])

    def get_sub_destinations(self):
        return "\n".join([p.sub_destination for p in self.sub_destination.all()])

    def __str__(self):
        return self.name


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
    PAYMENT = (
        ('CASH-ON-DELIVERY', 'CASH-ON-DELIVERY'),
        ('PING', 'PING'),
    )
    order_ref = models.CharField(max_length=200, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_state = models.CharField(max_length=50, choices=STATE, blank=True)

    client_name = models.CharField(max_length=200, blank=True)
    client_phone = PhoneNumberField(blank=True)
    registered_client = models.BooleanField(default=False)

    product_sku = models.CharField(max_length=200)
    product_color = models.CharField(max_length=200, default='UNDEFINED')
    product_option = models.CharField(max_length=200, default='UNDEFINED')
    product_shoe_size = models.CharField(max_length=200, default='UNDEFINED')
    product_clothing_size = models.CharField(max_length=200, default='UNDEFINED')
    product_price = models.DecimalField(max_digits=8, decimal_places=2)

    delivery_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    delivery_destination = models.ForeignKey('Destination', on_delete=models.CASCADE, blank=True, null=True)

    payment_method = models.CharField(max_length=50, choices=PAYMENT, blank=True, null=True)

    cart_ref = models.CharField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.client_name
