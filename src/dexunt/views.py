from django.shortcuts import render, redirect
from .models import Product, Slide, Banner
from django.http import Http404


def home(request):
    try:
        products = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    try:
        slides = Slide.objects.all()
    except Slide.DoesNotExist:
        raise Http404("Slide does not exist")

    try:
        banners = Banner.objects.all()
    except Tag.DoesNotExist:
        raise Http404("Banner does not exist")

    context = {
        'products': products,
        'banners': banners,
        'slides': slides,
    }
    return render(request, "dexunt/home.html", context)

