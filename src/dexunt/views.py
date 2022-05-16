from django.shortcuts import render, redirect
from django.http import Http404


def home(request):

    context = {
    }
    return render(request, "dexunt/home.html", context)

