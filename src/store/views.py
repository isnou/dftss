from django.shortcuts import render, redirect
# from sell.models import
from .models import Content, ShowCase, Product
from django.http import Http404
from django.db.models import Q
import random
import string


def serial_number_generator(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


def home(request):
    try:
        contents = Content.objects.all()
    except Content.DoesNotExist:
        raise Http404("No contents")
    try:
        showcases = ShowCase.objects.all().order_by('-position')
    except Content.DoesNotExist:
        raise Http404("No showcases")
    try:
        products = Product.objects.all().exclude(publish='False')
    except Content.DoesNotExist:
        raise Http404("No products")

    try:
        flash_collection = products.all().filter(collection='FLASH').order_by('?')[:8]
    except ShowCase.DoesNotExist:
        raise Http404("flash collection is empty")

    try:
        season_collection = products.all().filter(collection='SEASON').order_by('?')[:8]
    except ShowCase.DoesNotExist:
        raise Http404("season collection is empty")

    try:
        boxes_collection = products.all().filter(collection='BOX').order_by('?')[:8]
    except ShowCase.DoesNotExist:
        raise Http404("boxes collection is empty")

    try:
        latest_collection = products.all().order_by('-publish_date').exclude(publish='False').exclude(
            collection='SEASON').exclude(collection='FLASH').exclude(collection='BOX')[:8]
    except ShowCase.DoesNotExist:
        raise Http404("latest collection is empty")

    try:
        sell_collection = products.all().order_by('-sell_ranking').exclude(publish='False').exclude(
            collection='SEASON').exclude(collection='FLASH').exclude(collection='BOX')[:8]
    except ShowCase.DoesNotExist:
        raise Http404("sell collection is empty")

    try:
        rated_collection = products.all().order_by('-client_ranking').exclude(publish='False').exclude(
            collection='SEASON').exclude(collection='FLASH').exclude(collection='BOX')[:8]
    except ShowCase.DoesNotExist:
        raise Http404("sell collection is empty")

    context = {
        'rated_collection': rated_collection,
        'sell_collection': sell_collection,
        'latest_collection': latest_collection,
        'boxes_collection': boxes_collection,
        'season_collection': season_collection,
        'flash_collection': flash_collection,
        'showcases': showcases,
        'contents': contents,
    }
    return render(request, "store/home.html", context)


def store(request, collection):
    try:
        products = Product.objects.all().exclude(publish='False')
    except Content.DoesNotExist:
        raise Http404("No products")

    if collection == 'LATEST':
        product_collection = products.all().order_by('-publish_date').exclude(publish='False').exclude(
            collection='SEASON').exclude(collection='FLASH').exclude(collection='BOX')
    elif collection == 'SELL':
        product_collection = products.all().order_by('-sell_ranking').exclude(publish='False').exclude(
            collection='SEASON').exclude(collection='FLASH').exclude(collection='BOX')
    elif collection == 'RATE':
        product_collection = products.all().order_by('-client_ranking').exclude(publish='False').exclude(
            collection='SEASON').exclude(collection='FLASH').exclude(collection='BOX')
    else:
        product_collection = products.all().filter(collection=collection)
        product_collection = product_collection.order_by('?').all()

    context = {
        'product_collection': product_collection,
    }
    return render(request, "store/store-detail.html", context)


def product(request, product_id):
    try:
        all_products = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    selected_product = all_products.get(id=product_id)

    try:
        album = selected_product.album.all()
    except selected_product.DoesNotExist:
        raise Http404("Empty album")

    try:
        options = selected_product.option.all()
    except selected_product.DoesNotExist:
        raise Http404("No options")

    colors = None
    packs = None
    sizes = None

    for option in options:
        if option.type == 'COLOR':
            colors = option.parameter.all()
        elif option.type == 'PACK':
            packs = option.parameter.all()
        elif option.type == 'SIZE':
            sizes = option.parameter.all()

    related_products = all_products.filter(
        Q(filter_in=selected_product.filter_out) | Q(filter_flip=selected_product.filter_out))

    related_products = related_products.exclude(id=product_id).exclude(publish='False')
    related_products = related_products.order_by('?')[:8]

    context = {
        'selected_product': selected_product,
        'album': album,
        'options': options,
        'colors': colors,
        'packs': packs,
        'sizes': sizes,
        'related_products': related_products,
    }
    return render(request, "store/product-detail.html", context)
