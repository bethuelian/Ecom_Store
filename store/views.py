from django.shortcuts import render

# Create your views here.

def store(request):
    context = {}
    return render(request, 'storee/store.html', context)


def cart(request):
    context = {}
    return render(request, 'storee/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'storee/checkout.html', context)