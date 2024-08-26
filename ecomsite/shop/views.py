from django.shortcuts import render
from .models import Products
# Create your views here.


def index(request):
    products = Products.objects.all()
    
    # search 
    searched_product = request.GET.get('searched_product')

    if searched_product != '' and searched_product is not None:
        products = products.filter(title__icontains = searched_product)

    return render(request, 'shop/index.html', context= {'products': products})
