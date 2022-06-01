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


def orders_list(request, state):
    if state == 'ALL':
        orders = GroupOrder.objects.all().exclude(group_order_state='REQUEST').exclude(group_order_state='REMOVED')
    else:
        orders = 'EMPTY'

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


def update_orders(request, group_order_ref):
    if request.method == 'POST':
        sub_destination_name = request.POST.get('destination-name', False)
        option = request.POST.get('choose-option', False)
        account = request.POST.get('create-account', False)

    else:
        sub_destination_name = "undefined"
        option = 'UNCONFIRMED'
        account = 'none'

    group_order = GroupOrder.objects.get(group_order_ref=group_order_ref)
    group_order.group_order_state = option
    group_order.shipping_sub_destination = sub_destination_name

    if account == 'on':
        group_order.request = True
    else:
        group_order.request = False
    group_order.save()
    return redirect('orders-list')

