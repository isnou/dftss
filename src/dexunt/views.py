from django.shortcuts import render, redirect
from .models import Item, Slide, Banner, Category, SubCategory, Shop, Order, ShoppingCart
from django.http import Http404
from django.db.models import Q
from .forms import PreOrderForm, OrderForm
from django.template import RequestContext


def home(request):
    try:
        slides = Slide.objects.all()
    except Slide.DoesNotExist:
        raise Http404("Slide does not exist")

    try:
        banners = Banner.objects.all()
    except Banner.DoesNotExist:
        raise Http404("Banner does not exist")

    try:
        categories = Category.objects.all()
    except Category.DoesNotExist:
        raise Http404("Category does not exist")

    try:
        sub_categories = SubCategory.objects.all()
    except SubCategory.DoesNotExist:
        raise Http404("SubCategory does not exist")

    try:
        flash_shop = Shop.objects.get(id=1)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist")

    try:
        flash_list = flash_shop.product.all()
    except flash_shop.DoesNotExist:
        raise Http404("shop one is empty")
    flash_list = flash_list.order_by('?').all()[:12]

    try:
        season_collection_shop = Shop.objects.get(id=3)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist")

    try:
        season_collection_list = season_collection_shop.product.all()
    except season_collection_shop.DoesNotExist:
        raise Http404("shop three is empty")
    season_collection_list = season_collection_list.order_by('?').all()[:12]

    latest_items = Item.objects.all().order_by('-id')[:12]
    best_selling_items = Item.objects.all().order_by('-sell_rate')[:12]
    best_rated_items = Item.objects.all().order_by('-rate')[:12]

    context = {
        'banners': banners,
        'slides': slides,
        'categories': categories,
        'sub_categories': sub_categories,
        'flash_shop': flash_shop,
        'flash_list': flash_list,
        'season_collection_shop': season_collection_shop,
        'season_collection_list': season_collection_list,
        'latest_items': latest_items,
        'best_selling_items': best_selling_items,
        'best_rated_items': best_rated_items,
    }
    return render(request, "dexunt/home.html", context)


def store(request, number):
    try:
        shop = Shop.objects.get(id=number)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist")

    try:
        items = shop.product.all()
    except shop.DoesNotExist:
        raise Http404("shop one is empty")
    items = items.order_by('?').all()
    # total_items = items.count()
    # shown_items = shop.product.all()[0:4]
    # hidden_items = shop.product.all()[4:total_items]

    categories = shop.category.all()

    context = {
        'shop': shop,
        'items': items,
        'categories': categories,
    }
    return render(request, "dexunt/product.html", context)


def best_selling_store(request):
    try:
        items = Item.objects.all().order_by('-sell_rate')
    except Item.DoesNotExist:
        raise Http404("No items")

    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, "dexunt/product.html", context)


def best_rating_store(request):
    try:
        items = Item.objects.all().order_by('-rate')
    except Item.DoesNotExist:
        raise Http404("No items")

    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, "dexunt/product.html", context)


def latest_products(request):
    try:
        items = Item.objects.all().order_by('-id')
    except Item.DoesNotExist:
        raise Http404("No items")

    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, "dexunt/product.html", context)


def detail(request, key_id):
    try:
        item = Item.objects.get(id=key_id)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")

    try:
        albums = item.images.all()
    except item.DoesNotExist:
        raise Http404("Empty album")

    try:
        shoe_sizes = item.shoe_size.all()
    except item.DoesNotExist:
        raise Http404("Empty album")

    try:
        clothing_sizes = item.clothing_size.all()
    except item.DoesNotExist:
        raise Http404("Empty album")

    try:
        colors = item.color.all()
    except item.DoesNotExist:
        raise Http404("Empty album")

    try:
        options = item.option.all()
    except item.DoesNotExist:
        raise Http404("Empty album")

    category = item.category
    sub_category = item.sub_category

    related_items = Item.objects.all().filter(Q(category=category) | Q(sub_category=sub_category)).exclude(id=key_id)

    context = {
        'item': item,
        'albums': albums,
        'related_items': related_items,
        'shoe_sizes': shoe_sizes,
        'clothing_sizes': clothing_sizes,
        'colors': colors,
        'options': options,
    }
    return render(request, "dexunt/detail.html", context)


def shopping_cart(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")

    if request.method == 'POST':
        color = request.POST.get('color', False)
        option = request.POST.get('option', False)
        shoe_size = request.POST.get('shoe_size', False)
        clothing_size = request.POST.get('clothing_size', False)
    else:
        color = "none"
        option = "none"
        shoe_size = "none"
        clothing_size = "none"

    shop_cart = ShoppingCart(product_name=item.name,
                             shoe_size=shoe_size,
                             clothing_size=clothing_size,
                             color=color,
                             option=option,
                             )
    shop_cart.save()

    context = {
        'item': item,
        'shop_cart': shop_cart,
    }
    return render(request, "dexunt/shoping-cart.html", context)


def one_order_checkout(request, shopping_cart_id):
    try:
        shop_cart = ShoppingCart.objects.get(id=shopping_cart_id)
    except ShoppingCart.DoesNotExist:
        raise Http404("Item does not exist")

    # form = OrderForm(request.POST or None)
    if request.method == 'POST':
        client_name = request.POST.get('client_name', False)
        client_phone = request.POST.get('client_phone', False)
        quantity = request.POST.get('num-product2', False)
        delivery = request.POST.get('delivery', False)
        city = request.POST.get('city', False)
        town = request.POST.get('town', False)
        coupon = request.POST.get('coupon', False)
    else:
        quantity = "none"
        client_name = "none"
        client_phone = "none"
        delivery = "none"
        city = "none"
        town = "none"
        coupon = "none"

    order = Order(product_name=shop_cart.product_name,
                  shoe_size=shop_cart.shoe_size,
                  clothing_size=shop_cart.clothing_size,
                  color=shop_cart.color,
                  option=shop_cart.option,
                  quantity=quantity,

                  client_name=client_name,
                  client_phone=client_phone,
                  delivery=delivery,
                  city=city,
                  town=town,
                  coupon=coupon,
                  )
    order.save()

    context = {
        'order': order,
    }
    return render(request, "dexunt/check-out.html", context)
