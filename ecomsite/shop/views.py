from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    products = Products.objects.all()
    
    # search - always use pagination below search
    searched_product = request.GET.get('searched_product')

    if searched_product != '' and searched_product is not None:
        products = products.filter(title__icontains = searched_product)
        
    # pagination
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'shop/index.html', context= {'products': products})


def detail(request, id):
    product = Products.objects.get(id = id)
    
    return render(request, 'shop/detail.html', context= {'product': product})


def checkout(request):
    return render(request, 'shop/checkout.html')