from django.shortcuts import render, redirect
from .models import Item, Slide, Banner, Category, SubCategory, Shop
from django.http import Http404
from django.http import JsonResponse


def home(request):
    try:
        items = Item.objects.all()
    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    # total_items = Item.objects.count()
    items = items.order_by('?').all()

    try:
        slides = Slide.objects.all()
    except Slide.DoesNotExist:
        raise Http404("Slide does not exist")

    try:
        banners = Banner.objects.all()
    except Banner.DoesNotExist:
        raise Http404("Banner does not exist")

    try:
        categories = Category.objects.all()
    except Category.DoesNotExist:
        raise Http404("Category does not exist")

    try:
        sub_categories = SubCategory.objects.all()
    except SubCategory.DoesNotExist:
        raise Http404("SubCategory does not exist")

    try:
        shop_one = Shop.objects.get(id=1)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist")

    try:
        list_one = shop_one.product.all()
    except shop_one.DoesNotExist:
        raise Http404("shop one is empty")

    try:
        shop_two = Shop.objects.get(id=2)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist")

    try:
        list_two = shop_two.product.all()
    except shop_one.DoesNotExist:
        raise Http404("shop two is empty")

    try:
        shop_three = Shop.objects.get(id=3)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist")

    try:
        list_three = shop_three.product.all()
    except shop_one.DoesNotExist:
        raise Http404("shop three is empty")

    latest_items = Item.objects.filter(id=12).order_by('-id')[:10]

    context = {
        'items': items,
        'banners': banners,
        'slides': slides,
        'categories': categories,
        'sub_categories': sub_categories,
        'shop_one': shop_one,
        'list_one': list_one,
        'shop_two': shop_two,
        'list_two': list_two,
        'shop_three': shop_three,
        'list_three': list_three,
        'latest_items': latest_items,
    }
    return render(request, "dexunt/home.html", context)


def detail(request, key_id):
    try:
        item = Item.objects.get(id=key_id)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")

    try:
        albums = item.images.all()
    except Item.DoesNotExist:
        raise Http404("Empty album")

    shoe_sizes = item.shoe_size.all()
    clothing_sizes = item.clothing_size.all()
    options = item.option.all()
    colors = item.color.all()

    context = {
        'item': item,
        'albums': albums,
        'shoe_sizes': shoe_sizes,
        'clothing_sizes': clothing_sizes,
        'options': options,
        'colors': colors,
    }
    return render(request, "dexunt/detail.html", context)


def store(request, number):
    try:
        shop = Shop.objects.get(id=number)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist")

    try:
        items = shop.product.all()
    except shop.DoesNotExist:
        raise Http404("shop one is empty")
    total_items = items.count()
    shown_items = shop.product.all()[0:4]
    hidden_items = shop.product.all()[4:total_items]

    categories = shop.category.all()

    context = {
        'shop': shop,
        'items': items,
        'categories': categories,
        'shown_items': shown_items,
        'hidden_items': hidden_items,
    }
    return render(request, "dexunt/product.html", context)
