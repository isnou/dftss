from django.shortcuts import render, redirect
from .models import Product, Category, Tag
from django.http import Http404


def home(request):
    try:
        products = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    try:
        categories = Category.objects.all()
    except Category.DoesNotExist:
        raise Http404("Category does not exist")

    try:
        tags = Tag.objects.all()
    except Tag.DoesNotExist:
        raise Http404("Tag does not exist")

    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
    }
    return render(request, "dexunt/home.html", context)

