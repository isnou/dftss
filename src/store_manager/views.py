from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
# from sell.models import
from .models import Content, ShowCase, Product, Destination, Relation
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

    if collection == 'LATEST' or collection == 'SELL' or collection == 'RATE':
        page = request.GET.get('page', 1)
        paginator = Paginator(product_collection, 4)
        try:
            product_collection = paginator.page(page)
        except PageNotAnInteger:
            product_collection = paginator.page(1)
        except EmptyPage:
            product_collection = paginator.page(paginator.num_pages)
        paginate = True
    else:
        product_collection = product_collection.order_by('?').all()[:8]
        paginate = False

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

    context = {
        'product_collection': product_collection,
        'collection': collection,
        'paginate': paginate,
        'products': products,
        'products_quantity': products_quantity,
    }
    return render(request, "store-manager/store-detail.html", context)


def product(request, sku):
    try:
        all_products = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    selected_product = all_products.get(sku=sku)

    try:
        album = selected_product.image.all()
    except selected_product.DoesNotExist:
        raise Http404("Empty album")

    try:
        relations = Relation.objects.all()
    except Relation.DoesNotExist:
        raise Http404("No relations")

    options = all_products.filter(name=selected_product.name)

    if not options.exclude(publish='True').exists():
        options = None

    if relations.filter(name=selected_product.name).exists():
        related_products = relations.get(name=selected_product.name).product.all().order_by('?')[:8]
    else:
        related_products = None

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


def create_relations(request):
    Relation.objects.all().delete()
    try:
        all_products = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    for selected_product in all_products:
        new = Relation(name=selected_product.name)
        new.save()
        tags = selected_product.tag.split()
        for tag in tags:
            for product_to_add in all_products.filter(tag__contains=tag).exclude(name=selected_product.name) \
                    .exclude(publish='False'):
                new.product.add(product_to_add)

    for relation in Relation.objects.all():
        if relation.product.all().count() == 0:
            relation.delete()

    return redirect('home')


def sku_generator(request):
    try:
        all_products = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    for selected_product in all_products:
        selected_product.sku = serial_number_generator(8).upper()
        selected_product.save()

    return redirect('home')


def order(request, sku):
    shipping = ('standard', 'express')

    try:
        product_to_add = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    try:
        destinations = Destination.objects.all()
    except Destination.DoesNotExist:
        raise Http404("No destinations")

    if request.method == 'POST':
        quantity = request.POST.get('num-product2', False)
    else:
        quantity = 1

    new_item = Item(sku=product_to_add.sku,
                    name=product_to_add.name,
                    thumb=product_to_add.thumb,
                    quantity=quantity,
                    price=product_to_add.sell_price,
                    )
    new_item.save()

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

    if cart.item.all().filter(sku=new_item.sku).exists():
        existing_item = cart.item.get(sku=new_item.sku)
        existing_item.quantity += int(quantity)
        existing_item.save()
    else:
        cart.item.add(new_item)

    products = cart.item.all()
    products_quantity = cart.item.all().count()

    context = {
        'products': products,
        'products_quantity': products_quantity,
        'destinations': destinations,
        'shipping': shipping,
    }
    return render(request, "store-manager/shopping-cart.html", context)


def show_cart(request):
    shipping = ('standard', 'express')

    try:
        destinations = Destination.objects.all()
    except Destination.DoesNotExist:
        raise Http404("No destinations")

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

    context = {
        'products': products,
        'products_quantity': products_quantity,
        'destinations': destinations,
        'shipping': shipping,
    }
    return render(request, "store-manager/shopping-cart.html", context)


def delete_product(request, sku):
    session_id = request.session.get('session_id')
    cart = Order.objects.get(session_id=session_id)
    to_delete = cart.item.get(sku=sku)
    cart.item.remove(to_delete)
    return redirect('show-cart')


def add_quantity(request, sku):
    session_id = request.session.get('session_id')
    cart = Order.objects.get(session_id=session_id)
    item = cart.item.get(sku=sku)
    item.quantity += 1
    item.save()
    return redirect('show-cart')


def remove_quantity(request, sku):
    session_id = request.session.get('session_id')
    cart = Order.objects.get(session_id=session_id)
    item = cart.item.get(sku=sku)
    if item.quantity > 0:
        item.quantity -= 1
        item.save()
    return redirect('show-cart')


def delete_product_to_home(request, sku):
    session_id = request.session.get('session_id')
    cart = Order.objects.get(session_id=session_id)
    to_delete = cart.item.get(sku=sku)
    cart.item.remove(to_delete)
    return redirect('home')
