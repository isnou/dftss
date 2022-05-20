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
        flash_shop = Shop.objects.get(id=1)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist")

    try:
        flash_list = flash_shop.product.all()
    except flash_shop.DoesNotExist:
        raise Http404("shop one is empty")

    try:
        season_collection_shop = Shop.objects.get(id=3)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist")

    try:
        season_collection_list = season_collection_shop.product.all()
    except season_collection_shop.DoesNotExist:
        raise Http404("shop three is empty")
    season_collection_list = season_collection_list.order_by('?').all()

    latest_items = Item.objects.all().order_by('-id')[:15]
    best_selling_items = Item.objects.all().order_by('-sell_rate')[:15]
    best_rated_items = Item.objects.all().order_by('-rate')[:15]

    context = {
        'items': items,
        'banners': banners,
        'slides': slides,
        'categories': categories,
        'sub_categories': sub_categories,
        'flash_shop': flash_shop,
        'flash_list': flash_list,
        'season_collection_shop': season_collection_shop,
        'season_collection_list': season_collection_list,
        'latest_items': latest_items,
        'best_selling_items': best_selling_items,
        'best_rated_items': best_rated_items,
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


def best_selling_store(request, number):
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


def best_rating_store(request, number):
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


def latest_products(request, number):
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