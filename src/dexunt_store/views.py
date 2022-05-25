from django.shortcuts import render, redirect
from .models import Content, ShowCase, Product
from dexunt_sell.models import Order, Destination
from django.http import Http404
from django.db.models import Q
import random
import string
from .forms import PreOrderForm, OrderForm


def serial_number_generator(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


def home(request):
    try:
        slides = Content.objects.all()[0:3]
    except Content.DoesNotExist:
        raise Http404("No Slides")
    try:
        banners = Content.objects.all()[3:6]
    except Content.DoesNotExist:
        raise Http404("No Banners")

    try:
        flash_collection_store = ShowCase.objects.get(collection='FLASH')
    except ShowCase.DoesNotExist:
        raise Http404("flash collection store does not exist")

    try:
        flash_collection = Product.objects.all().filter(collection='FLASH')
    except flash_collection_store.DoesNotExist:
        raise Http404("flash collection store is empty")
    flash_collection = flash_collection.order_by('?').all()[:8]

    try:
        season_collection_store = ShowCase.objects.get(collection='SEASON')
    except ShowCase.DoesNotExist:
        raise Http404("season collection store does not exist")

    try:
        season_collection = Product.objects.all().filter(collection='SEASON')
    except season_collection_store.DoesNotExist:
        raise Http404("season collection store is empty")
    season_collection = season_collection.order_by('?').all()[:12]

    try:
        latest_collection_store = ShowCase.objects.get(collection='LATEST')
    except ShowCase.DoesNotExist:
        raise Http404("latest collection store does not exist")
    latest_collection = Product.objects.all().order_by('-publish_rate').exclude(publish='False').exclude(
        collection='SEASON').exclude(collection='FLASH')[:8]

    try:
        best_selling_collection_store = ShowCase.objects.get(collection='SELL')
    except ShowCase.DoesNotExist:
        raise Http404("best selling collection store does not exist")
    best_selling_collection = Product.objects.all().order_by('-sell_rate').exclude(publish='False').exclude(
        collection='SEASON').exclude(collection='FLASH')[:12]

    try:
        best_rated_collection_store = ShowCase.objects.get(collection='RATE')
    except ShowCase.DoesNotExist:
        raise Http404("best rated collection store does not exist")
    best_rated_collection = Product.objects.all().order_by('-rate').exclude(publish='False').exclude(
        collection='SEASON').exclude(collection='FLASH')[:12]

    context = {
        'slides': slides,
        'banners': banners,

        'flash_collection_store': flash_collection_store,
        'season_collection_store': season_collection_store,
        'latest_collection_store': latest_collection_store,
        'best_selling_collection_store': best_selling_collection_store,
        'best_rated_collection_store': best_rated_collection_store,

        'flash_collection': flash_collection,
        'season_collection': season_collection,
        'latest_collection': latest_collection,
        'best_selling_collection': best_selling_collection,
        'best_rated_collection': best_rated_collection,
    }
    return render(request, "dexunt-store/home.html", context)


def store_detail(request, collection):
    try:
        collection_store = ShowCase.objects.get(collection=collection)
    except ShowCase.DoesNotExist:
        raise Http404("flash collection store does not exist")

    if collection == 'FLASH' or collection == 'SEASON':
        product_collection = Product.objects.all().filter(collection=collection)
        product_collection = product_collection.order_by('?').all()[:8]
    elif collection == 'LATEST':
        product_collection = Product.objects.all().order_by('-publish_rate').exclude(publish='False').exclude(
            collection='SEASON').exclude(collection='FLASH')
    elif collection == 'SELL':
        product_collection = Product.objects.all().order_by('-sell_rate').exclude(publish='False').exclude(
            collection='SEASON').exclude(collection='FLASH')
    elif collection == 'RATE':
        product_collection = Product.objects.all().order_by('-rate').exclude(publish='False').exclude(
            collection='SEASON').exclude(collection='FLASH')
    else:
        product_collection = 'none'

    categories = collection_store.category.all()

    context = {
        'collection_store': collection_store,
        'product_collection': product_collection,
        'categories': categories,
    }
    return render(request, "dexunt-store/store-detail.html", context)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    try:
        album = product.images.all()
    except product.DoesNotExist:
        raise Http404("Empty album")

    try:
        shoe_sizes = product.shoe_size.all()
    except product.DoesNotExist:
        raise Http404("No sizes")

    try:
        clothing_sizes = product.clothing_size.all()
    except product.DoesNotExist:
        raise Http404("No sizes")

    try:
        colors = product.color.all()
    except product.DoesNotExist:
        raise Http404("No colors")

    try:
        options = product.option.all()
    except product.DoesNotExist:
        raise Http404("No options")

    category = product.category
    sub_category = product.sub_category
    tag = product.tag

    related_products = Product.objects.all().filter(Q(category=category) | Q(sub_category=sub_category) | Q(tag=tag)). \
        exclude(id=product_id).exclude(publish='False')

    context = {
        'product': product,
        'album': album,
        'related_products': related_products,
        'shoe_sizes': shoe_sizes,
        'clothing_sizes': clothing_sizes,
        'colors': colors,
        'options': options,
    }
    return render(request, "dexunt-store/product-detail.html", context)


def shopping_cart(request, product_sku):
    payments = ('CASH-ON-DELIVERY', 'PING')
    shipping = ('standard', 'express')

    order_ref = serial_number_generator(8)
    cart_ref = serial_number_generator(8)

    try:
        product = Product.objects.get(sku=product_sku)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    try:
        destinations = Destination.objects.all()
    except Destination.DoesNotExist:
        raise Http404("No destinations")

    if request.method == 'POST':
        color = request.POST.get('color', False)
        option = request.POST.get('option', False)
        shoe_size = request.POST.get('shoe_size', False)
        clothing_size = request.POST.get('clothing_size', False)
    else:
        color = "none"
        option = "none"
        shoe_size = "none"
        clothing_size = "none"

    order = Order(order_ref=order_ref,
                  product_sku=product.sku,
                  product_name=product.name,
                  product_color=color,
                  product_option=option,
                  product_shoe_size=shoe_size,
                  product_clothing_size=clothing_size,
                  cart_ref=cart_ref,
                  )
    order.save()

    context = {
        'product': product,
        'order_ref': order_ref,
        'destinations': destinations,
        'payments': payments,
        'shipping': shipping,
    }
    return render(request, "dexunt-store/shopping-cart.html", context)


def check_out(request, order_ref):

    try:
        order = Order.objects.get(order_ref=order_ref)
    except Order.DoesNotExist:
        raise Http404("Product does not exist")

    if request.method == 'POST':
        client_name = request.POST.get('client_name', False)
        client_phone = request.POST.get('client_phone', False)
        quantity = request.POST.get('num-product2', False)
        product_price = request.POST.get('total', False)
        destination = request.POST.get('destination', False)
        shipping = request.POST.get('shipping', False)
        coupon = request.POST.get('coupon', False)


    else:
        client_name = "none"
        client_phone = "none"
        quantity = "none"
        product_price = "none"
        destination = "none"
        shipping = "none"
        coupon = "none"

    context = {
    }
    return render(request, "dexunt-store/home.html", context)
