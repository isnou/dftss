from django.shortcuts import render, redirect
from .models import Content, Category, SubCategory, ShowCase, Product
from django.http import Http404
from django.db.models import Q
from .forms import PreOrderForm, OrderForm


def home(request):
    try:
        content = Content.objects.all()
    except Content.DoesNotExist:
        raise Http404("No Content")

    try:
        categories = Category.objects.all()
    except Category.DoesNotExist:
        raise Http404("Category does not exist")

    try:
        sub_categories = SubCategory.objects.all()
    except SubCategory.DoesNotExist:
        raise Http404("SubCategory does not exist")

    try:
        flash_shop = ShowCase.objects.get(id=1)
    except ShowCase.DoesNotExist:
        raise Http404("Shop does not exist")

    try:
        flash_list = flash_shop.product.all()
    except flash_shop.DoesNotExist:
        raise Http404("shop one is empty")
    flash_list = flash_list.order_by('?').all()[:12]

    try:
        season_collection_shop = ShowCase.objects.get(id=3)
    except ShowCase.DoesNotExist:
        raise Http404("Shop does not exist")

    try:
        season_collection_list = season_collection_shop.product.all()
    except season_collection_shop.DoesNotExist:
        raise Http404("shop three is empty")
    season_collection_list = season_collection_list.order_by('?').all()[:12]

    latest_items = Product.objects.all().order_by('-id')[:12]
    best_selling_items = Product.objects.all().order_by('-sell_rate')[:12]
    best_rated_items = Product.objects.all().order_by('-rate')[:12]

    context = {
        'content': content,
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
    return render(request, "dexunt_store/home.html", context)
