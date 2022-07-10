from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
# from sell.models import
from .models import Content, ShowCase, Product, Destination
from sell_manager.models import Order, Item
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

    if not request.session.get('session_id', None):
        gen_ref = serial_number_generator(8).upper()
        gen_session_id = serial_number_generator(8).upper()
        request.session['session_id'] = gen_session_id
        cart = Order(ref=gen_ref,
                     session_id=gen_session_id,
                     )
        cart.save()
    else:
        session_id = request.session.get('session_id')
        if Order.objects.all().filter(session_id=session_id).exists():
            cart = Order.objects.get(session_id=session_id)
        else:
            gen_ref = serial_number_generator(8).upper()
            cart = Order(ref=gen_ref,
                         session_id=session_id,
                         )
            cart.save()

    products = cart.item.all()
    products_quantity = cart.item.all().count()

    context = {
        'rated_collection': rated_collection,
        'sell_collection': sell_collection,
        'latest_collection': latest_collection,
        'boxes_collection': boxes_collection,
        'season_collection': season_collection,
        'flash_collection': flash_collection,
        'showcases': showcases,
        'contents': contents,
        'products': products,
        'products_quantity': products_quantity,
    }
    return render(request, "store-manager/home.html", context)


def product(request, product_id):
    try:
        all_products = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    selected_product = all_products.get(id=product_id)

    try:
        album = selected_product.image.all()
    except selected_product.DoesNotExist:
        raise Http404("Empty album")

    options = all_products.filter(name=selected_product.name)

    if not options.exclude(publish='True').exists():
        options = None

    tags = selected_product.tag.split()
    related_products = []
    for tag in tags:
        related_products = all_products.filter(tag__contains=tag)

    # related_products = all_products.filter(
    #    Q(filter=selected_product.filter) | Q(flip=selected_product.filter))
    # related_products = related_products.exclude(name=selected_product.name).exclude(publish='False')
    # related_products = related_products.order_by('?')[:8]

    if not request.session.get('session_id', None):
        gen_ref = serial_number_generator(8).upper()
        gen_session_id = serial_number_generator(8).upper()
        request.session['session_id'] = gen_session_id
        cart = Order(ref=gen_ref,
                     session_id=gen_session_id,
                     )
        cart.save()
    else:
        session_id = request.session.get('session_id')
        cart = Order.objects.get(session_id=session_id)

    products = cart.item.all()
    products_quantity = cart.item.all().count()

    if products.filter(sku=selected_product.sku).exists():
        quantity_value = cart.item.get(sku=selected_product.sku).quantity
        product_exists = True
    else:
        quantity_value = 1
        product_exists = False

    context = {
        'selected_product': selected_product,
        'album': album,
        'options': options,
        'related_products': related_products,
        'products': products,
        'products_quantity': products_quantity,
        'quantity_value': quantity_value,
        'product_exists': product_exists,
    }
    return render(request, "store-manager/product-detail.html", context)
