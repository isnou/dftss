from django.shortcuts import render, redirect
# from sell.models import
from .models import Content
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
        raise Http404("No content")

    context = {
        'contents': contents,
    }
    return render(request, "store/home.html", context)
