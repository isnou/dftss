from django.shortcuts import render, redirect
from .models import Item, Slide, Banner, Category, Tag
from django.http import Http404


def home(request):
    try:
        items = Item.objects.all()
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
        album = item.images.all()
    except Item.DoesNotExist:
        raise Http404("Empty album")

    context = {
        'item': item,
        'album': album,
    }
    return render(request, "dexunt/detail.html", context)
