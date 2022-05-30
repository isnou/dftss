from django.shortcuts import render, redirect
from .models import GroupOrder, Destination, Coupon
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def manager_home(request):
    orders_quantity = 0

    context = {
        'orders_quantity': orders_quantity,
    }
    return render(request, "dexunt-sell/manager-dashboard.html", context)


def orders_list(request):
    orders = GroupOrder.objects.all().exclude(group_order_state='REQUEST')
    page = request.GET.get('page', 1)

    paginator = Paginator(orders, 10)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {
        'orders': orders,
    }

    return render(request, "dexunt-sell/orders.html", context)


def orders_details(request):
    orders_quantity = 0

    context = {
        'orders_quantity': orders_quantity,
    }
    return render(request, "dexunt-sell/orders-details.html", context)
