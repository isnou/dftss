from django.shortcuts import render, redirect
from dexunt_sell.models import Order, Destination, GroupOrder, Coupon
from django.http import Http404
from django.db.models import Q
import random
import string


def serial_number_generator(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


def home(request):
    order_ref = 0

    context = {
        'order_ref': order_ref,
    }
    return render(request, "store/home.html", context)
