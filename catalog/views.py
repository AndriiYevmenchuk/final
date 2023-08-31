from django.shortcuts import render, redirect
from .models import *
from .filters import *
from django.http import *
from django.template.loader import render_to_string


def index(request):
    products = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    return render(request, 'catalog/index.html', {
        'title': 'Каталог',
        'app': 'catalog',
        'page': 'index',
        'all_categories': Category.objects.all(),
        'all_brands': Brand.objects.all(),
        'all_colors': Color.objects.all(),
        'all_sizes': Size.objects.all(),
        'all_products': products,
        'myFilter': myFilter
    })


def details(request, product_id):
    transit_data = dict()
    transit_data['title'] = 'Детальна інформація'
    target_product = Product.objects.get(id=product_id)
    if request.method == 'GET':
        transit_data['target_product']= target_product
        return render(request, 'catalog/product_details.html', context=transit_data)
    elif request.method == 'POST':
        return redirect('/catalog')


