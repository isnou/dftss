from django.shortcuts import render, redirect
# from sell.models import
from .models import Content, ShowCase, Product
from django.http import Http404
from django.db.models import Q
import random
import string


def serial_number_generator(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


def home(request):
    try:
        contents = Content.objects.all()
    except Content.DoesNotExist:
        raise Http404("No contents")
    try:
        showcases = ShowCase.objects.all().order_by('-position')
    except Content.DoesNotExist:
        raise Http404("No showcases")
    try:
        products = Product.objects.all()
    except Content.DoesNotExist:
        raise Http404("No products")

    try:
        flash_collection = products.all().filter(collection='FLASH')
    except ShowCase.DoesNotExist:
        raise Http404("flash collection is empty")

    try:
        season_collection = products.get(collection='SEASON')
    except ShowCase.DoesNotExist:
        raise Http404("season collection is empty")

    try:
        boxes_collection = products.get(collection='BOX')
    except ShowCase.DoesNotExist:
        raise Http404("boxes collection is empty")

    try:
        latest_collection = products.all().order_by('-sell_ranking').exclude(publish='False').exclude(
            collection='SEASON').exclude(collection='FLASH').exclude(collection='BOX')
    except ShowCase.DoesNotExist:
        raise Http404("latest collection is empty")

    context = {
        'latest_collection': latest_collection,
        'boxes_collection': boxes_collection,
        'season_collection': season_collection,
        'flash_collection': flash_collection,
        'showcases': showcases,
        'contents': contents,
    }
    return render(request, "store/home.html", context)
