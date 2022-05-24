from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class SubDestination(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=200, unique=True)
    sub_destination = models.ManyToManyField(SubDestination, blank=True)
    delivery_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    company_name = models.CharField(max_length=200, unique=True)
    prices = models.ManyToManyField(Destination, blank=True)

    class Meta:
        verbose_name_plural = "Delivery"

    def __str__(self):
        return self.company_name


class Order(models.Model):
    STATE = (
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
    order_state = models.CharField(max_length=50, choices=STATE)
    grouped_order = models.BooleanField(default=False)

    client_name = models.CharField(max_length=200, blank=True)
    client_phone = PhoneNumberField(blank=True)
    registered_client = models.BooleanField(default=False)

    product_sku = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)

    delivery_price = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_destination = models.ForeignKey('Destination', on_delete=models.CASCADE, blank=True)

    payment_method = models.CharField(max_length=50, choices=PAYMENT)

    def __str__(self):
        return self.client_name
