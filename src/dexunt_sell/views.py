from django.http import Http404
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


def orders_details(request, group_order_ref):
    group_order = GroupOrder.objects.get(group_order_ref=group_order_ref)
    try:
        orders = group_order.order.all()
    except group_order.DoesNotExist:
        raise Http404("No orders")

    page = request.GET.get('page', 1)

    paginator = Paginator(orders, 10)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {
        'group_order': group_order,
        'orders': orders,
    }
    return render(request, "dexunt-sell/orders-details.html", context)


def delete_order(request, group_order_ref, order_ref):
    group_order = GroupOrder.objects.get(group_order_ref=group_order_ref)
    order = group_order.order.get(order_ref=order_ref)
    group_order.total_price = group_order.total_price - (order.product_price * order.quantity)
    group_order.save()
    order.delete()
    return redirect('orders-details', group_order_ref=group_order_ref)


def delete_orders(request, group_order_ref):
    group_order = GroupOrder.objects.get(group_order_ref=group_order_ref)
    group_order.group_order_state = 'REMOVED'
    group_order.save()
    return redirect('orders-list')
