from django.shortcuts import render, redirect
from .models import Item, Slide, Banner, Category, Tag
from django.http import Http404
from django.http import JsonResponse


def home(request):
    try:
        items = Item.objects.all()
    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    total_items = Item.objects.count()

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
        'posts': items,
        'banners': banners,
        'slides': slides,
        'categories': categories,
        'tags': tags,
        'total_obj': total_items,
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


def index(request):
    post_obj = Item.objects.all()[0:4]
    total_obj = Item.objects.count()
    return render(request, 'dexunt/index.html', context={'posts': post_obj, 'total_obj': total_obj})


def load_more(request):
    loaded_item = request.GET.get('loaded_item')
    loaded_item_int = int(loaded_item)
    limit = 4
    post_obj = list(Item.objects.values()[loaded_item_int:loaded_item_int + limit])
    data = {'posts': post_obj}
    return JsonResponse(data=data)
