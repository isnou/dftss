from django.shortcuts import render, redirect
from .models import Item, Slide, Banner
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

    context = {
        'items': items,
        'banners': banners,
        'slides': slides,
    }
    return render(request, "dexunt/home.html", context)

