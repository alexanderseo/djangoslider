from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def modules (request):
    return render(request, 'main/modules.html')

def portfolio (request):
    return render(request, 'main/portfolio.html')

def products (request):
    return render(request, 'main/products.html')

def reviews (request):
    return render(request, 'main/reviews.html')