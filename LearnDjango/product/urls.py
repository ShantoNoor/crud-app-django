from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('details/<int:id>', ProductDetailView.as_view(), name='product_details'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    # path('about/', about_view, name='about'),
    # path('contact/', contact_view, name='contact')
]
