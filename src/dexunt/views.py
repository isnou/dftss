from django.shortcuts import render, redirect
from .models import Product, Category


def home(request):
    try:
        products = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    try:
        categories = Category.objects.all()
    except Category.DoesNotExist:
        raise Http404("Category does not exist")

    context = {
        'products': products,
        'products.product_banner_image': products.product_banner_image,
        'categories': categories,
    }
    return render(request, "dexunt/home.html", context)

