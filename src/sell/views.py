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
    if product_sku != 'show':
        if request.method == 'POST':
            product_name = request.POST.get('product_name', False)
    order_ref = 0

    context = {
        'order_ref': order_ref,
    }
    return render(request, "sell/products-list.html", context)


def add_product(request):
    try:
        colors = Color.objects.all()
    except Color.DoesNotExist:
        raise Http404("No colors")
    try:
        sizes = Size.objects.all()
    except Size.DoesNotExist:
        raise Http404("No sizes")
    try:
        packs = Pack.objects.all()
    except Pack.DoesNotExist:
        raise Http404("No packs")
    try:
        brands = Brand.objects.all()
    except Brand.DoesNotExist:
        raise Http404("No brands")
    product_sku = serial_number_generator(8)

    context = {
        'colors': colors,
        'sizes': sizes,
        'packs': packs,
        'brands': brands,
        'product_sku': product_sku,
    }
    return render(request, "sell/add-product.html", context)

