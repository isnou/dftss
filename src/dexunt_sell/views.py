from django.shortcuts import render, redirect


def manager_home(request):
    orders_quantity = 0

    context = {
        'orders_quantity': orders_quantity,
    }
    return render(request, "dexunt-sell/manager-dashboard.html", context)


def orders(request):
    orders_quantity = 0

    context = {
        'orders_quantity': orders_quantity,
    }
    return render(request, "dexunt-sell/orders.html", context)


def orders_details(request):
    orders_quantity = 0

    context = {
        'orders_quantity': orders_quantity,
    }
    return render(request, "dexunt-sell/orders-details.html", context)
