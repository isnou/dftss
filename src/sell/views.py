from django.shortcuts import render, redirect
from store.models import Content, Album, Size, Color, Pack, Brand, Product, Box, Collection, ShowCase
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
    return render(request, "sell/dashboard.html", context)


def products_list(request, product_sku):
    order_ref = 0

    context = {
        'order_ref': order_ref,
    }
    return render(request, "sell/products-list.html", context)


def add_product(request):
    product_sku = serial_number_generator(8)
    context = {
        'product_sku': product_sku,
    }
    return render(request, "sell/add-product.html", context)

