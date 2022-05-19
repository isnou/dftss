from django.shortcuts import render, redirect
from .models import Item, Slide, Banner, Category, Tag, Shop
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
    except Tag.DoesNotExist:
        raise Http404("Banner does not exist")

    try:
        categories = Category.objects.all()
    except Category.DoesNotExist:
        raise Http404("Category does not exist")

    try:
        tags = Tag.objects.all()
    except Tag.DoesNotExist:
        raise Http404("Tag does not exist")

    try:
        shop_one = Shop.objects.get(id=1)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist")

    try:
        list_one = shop_one.product.all()
    except shop_one.DoesNotExist:
        raise Http404("shop one is empty")

    context = {
        'items': items,
        'banners': banners,
        'slides': slides,
        'categories': categories,
        'tags': tags,
        'shop_one': shop_one,
        'list_one': list_one,
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

    tags = item.tag.all()
    for tag in tags:
        related_items = Item.objects.filter(tag=tag)

    context = {
        'item': item,
        'albums': albums,
        'shoe_sizes': shoe_sizes,
        'clothing_sizes': clothing_sizes,
        'options': options,
        'colors': colors,
        'related_items': related_items,
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

    context = {
        'shop': shop,
        'items': items,
    }
    return render(request, "dexunt/product.html", context)
