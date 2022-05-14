from django.shortcuts import render

from django.shortcuts import render,redirect
from django.http import Http404


def main(request):

    return render(request, "base_layout.html")