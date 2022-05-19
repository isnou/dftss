from django.shortcuts import render, redirect
from .models import Item, Slide, Banner, Category, Tag
from django.http import Http404
from django.http import JsonResponse
from django.views.generic import View, TemplateView


def home(request):
    try:
        items = Item.objects.all()
    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    # total_items = Item.objects.count()

    try:
        slides = Slide.objects.all()
    except Slide.DoesNotExist:
        raise Http404("Slide does not exist")

    try:
        banners = Banner.objects.all()
    except Tag.DoesNotExist:
        raise Http404("Banner does not exist")

    try:
        categories = Category.objects.all()
    except Category.DoesNotExist:
        raise Http404("Category does not exist")

    try:
        tags = Tag.objects.all()
    except Tag.DoesNotExist:
        raise Http404("Tag does not exist")

    context = {
        'items': items,
        'banners': banners,
        'slides': slides,
        'categories': categories,
        'tags': tags,
    }
    return render(request, "dexunt/home.html", context)


def detail(request, key_id):
    try:
        item = Item.objects.get(id=key_id)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")

    try:
        albums = item.images.all()
    except Item.DoesNotExist:
        raise Http404("Empty album")

    shoe_sizes = item.shoe_size.all()
    clothing_sizes = item.clothing_size.all()
    options = item.option.all()
    colors = item.color.all()

    tags = item.tag.all()
    for tag in tags:
        related_items = Item.objects.filter(tag=tag)

    context = {
        'item': item,
        'albums': albums,
        'shoe_sizes': shoe_sizes,
        'clothing_sizes': clothing_sizes,
        'options': options,
        'colors': colors,
        'related_items': related_items,
    }
    return render(request, "dexunt/detail.html", context)


def MainView(TemplateView):
    template_name = 'dexunt/index.html'



def PostJsonListView(View):
    def get(self, *args, **kwargs):
        print(kwargs)
        upper = kwargs.get('num_posts')
        lower = upper - 3
        posts = list(Item.objects.values()[lower:upper])
        posts_size = len(Item.objects.all())
        max_size = True if upper >= posts_size else False
        return JsonResponse({'data': posts, 'max': max_size}, safe=False)
