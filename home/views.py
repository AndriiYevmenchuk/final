from django.shortcuts import *
from catalog.models import Product
from .filters import *


def index(request):
    return render(request, 'home/index.html', {
        'title':'Головна',
        'page':'index',
        'app':'home'
    })


def about(request):
    return render(request, 'home/about.html', {
        'title':'Про сайт',
        'page':'about',
        'app':'home'
    })

def contacts(request):
    return render(request, 'home/contacts.html', {
        'title':'Контакти',
        'page':'contacts',
        'app':'home'
    })


def search(request):
    query =request.GET['query']
    all_products = Product.objects.filter(name__icontains=query)
    myFilter = ProductFilter(request.GET, queryset=all_products)
    products = myFilter.qs
    params={'all_products': all_products,
            'title':'результати пошуку за запитом ' + query,
            'myFilter': myFilter
            }
    return render(request, 'home/search.html', params)
