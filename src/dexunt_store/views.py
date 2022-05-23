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
        flash_collection_store = ShowCase.objects.get(id=1)
    except ShowCase.DoesNotExist:
        raise Http404("flash collection store does not exist")

    try:
        flash_collection_store = flash_collection_store.product.all()
    except flash_collection_store.DoesNotExist:
        raise Http404("flash collection store is empty")
    flash_collection_store = flash_collection_store.order_by('?').all()[:12]

    try:
        season_collection_store = ShowCase.objects.get(id=2)
    except ShowCase.DoesNotExist:
        raise Http404("season collection store does not exist")

    try:
        season_collection_store = season_collection_store.product.all()
    except season_collection_store.DoesNotExist:
        raise Http404("season collection store is empty")
    season_collection_store = season_collection_store.order_by('?').all()[:12]

    latest_collection_store = Product.objects.all().order_by('-id')[:12]
    best_selling_collection_store = Product.objects.all().order_by('-sell_rate')[:12]
    best_rated_collection_store = Product.objects.all().order_by('-rate')[:12]

    context = {
        'content': content,
        'categories': categories,
        'sub_categories': sub_categories,
        'flash_collection_store': flash_collection_store,
        'season_collection_store': season_collection_store,
        'latest_collection_store': latest_collection_store,
        'best_selling_collection_store': best_selling_collection_store,
        'best_rated_collection_store': best_rated_collection_store,
    }
    return render(request, "dexunt_store/home.html", context)
