from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product-list'),
    path('products/create/', views.product_create, name='product-create'),
]
