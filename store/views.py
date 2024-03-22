from django.shortcuts import render
from .models import *

# Create your views here.

def store(request):
    products =Product.objects.all()
    context = {'products': products}
    return render(request, 'storee/store.html', context)


def cart(request):
    context = {}
    return render(request, 'storee/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'storee/checkout.html', context)


