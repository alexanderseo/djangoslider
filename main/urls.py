from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('modules/', views.modules, name='modules'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('products/', views.products, name='products'),
    path('reviews/', views.reviews, name='reviews'),
    path('text-page/', views.textpage, name='textpage'),
    path('account/', views.account, name='account'),
]