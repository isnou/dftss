from django.shortcuts import render, redirect
from .models import Item, Slide, Banner, Category, Tag
from django.http import Http404
from django.http import JsonResponse


def home(request):
    try:
        items = Item.objects.all()[0:2]
    except Item.DoesNotExist:
        raise Http404("Item does not exist")

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

    context = {
        'items': items,
        'banners': banners,
        'slides': slides,
        'categories': categories,
        'tags': tags,
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
