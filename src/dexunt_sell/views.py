from django.shortcuts import render, redirect
from .models import GroupOrder, Destination, Coupon
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def manager_home(request):
    orders_quantity = 0

    context = {
        'orders_quantity': orders_quantity,
    }
    return render(request, "dexunt-sell/dev-manager-dashboard.html", context)


def orders(request):
    orders_list = GroupOrder.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(orders_list, 10)
    try:
        orders_object = paginator.page(page)
    except PageNotAnInteger:
        orders_object = paginator.page(1)
    except EmptyPage:
        orders_object = paginator.page(paginator.num_pages)

    context = {
        'orders_object': orders_object,
    }

    return render(request, "dexunt-sell/orders.html", context)


def orders_details(request):
    orders_quantity = 0

    context = {
        'orders_quantity': orders_quantity,
    }
    return render(request, "dexunt-sell/orders-details.html", context)
