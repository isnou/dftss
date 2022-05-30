from django.shortcuts import render, redirect


def manager_home(request):
    orders_quantity = 0

    context = {
        'orders_quantity': orders_quantity,
    }
    return render(request, "dexunt-sell/all-orders-list.html", context)


def all_orders_list(request):
    orders_quantity = 0

    context = {
        'orders_quantity': orders_quantity,
    }
    return render(request, "dexunt-sell/all-orders-list.html", context)
