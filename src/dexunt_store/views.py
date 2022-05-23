from django.shortcuts import render, redirect
from .models import Content, Category, SubCategory, ShowCase, Product
from django.http import Http404
from django.db.models import Q
from .forms import PreOrderForm, OrderForm


def home(request):
    try:
        slides = Content.objects.all()[0:3]
    except Content.DoesNotExist:
        raise Http404("No Slides")
    try:
        banners = Content.objects.all()[3:6]
    except Content.DoesNotExist:
        raise Http404("No Banners")

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

    try:
        latest_collection_store = ShowCase.objects.get(id=3)
    except ShowCase.DoesNotExist:
        raise Http404("latest collection store does not exist")

    try:
        best_selling_collection_store = ShowCase.objects.get(id=4)
    except ShowCase.DoesNotExist:
        raise Http404("best selling collection store does not exist")

    try:
        best_rated_collection_store = ShowCase.objects.get(id=5)
    except ShowCase.DoesNotExist:
        raise Http404("best rated collection store does not exist")

    latest_collection = Product.objects.all().order_by('-id')[:12]
    best_selling_collection = Product.objects.all().order_by('-sell_rate')[:12]
    best_rated_collection = Product.objects.all().order_by('-rate')[:12]

    context = {
        'slides': slides,
        'banners': banners,

        'flash_collection_store': flash_collection_store,
        'season_collection_store': season_collection_store,
        'latest_collection_store': latest_collection_store,
        'best_selling_collection_store': best_selling_collection_store,
        'best_rated_collection_store': best_rated_collection_store,

        'latest_collection': latest_collection,
        'best_selling_collection': best_selling_collection,
        'best_rated_collection': best_rated_collection,
    }
    return render(request, "dexunt_store/home.html", context)
