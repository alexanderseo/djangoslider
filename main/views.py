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

def textpage (request):
    return render(request, 'main/text-page.html')

def account (request):
    return render(request, 'main/account.html')

def monitoring (request):
    return render(request, 'main/monitoring.html')

def boost (request):
    return render(request, 'main/boost.html')

def masterserver (request):
    return render(request, 'main/masterserver.html')

