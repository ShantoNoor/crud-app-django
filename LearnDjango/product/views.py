from django.db import models
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Create your views here.

# def home_view(request):
#     return render(request, 'home.html', context={'data': 'home page data', 'name_list': ['rohim', 'Korim', 'Jamar']})

# def about_view(request):
#     return render(request, 'about.html', context={'data': 'About Page Data'})

# def contact_view(request):
#     return render(request, 'contact.html', context={'data': 'Contact Page Data'})

class ProductListView(ListView): # <app_name>/<model_name>_list.html
    queryset = Product.objects.all()
    template_name = 'home.html'

class ProductDetailView(DetailView): # <app_name>/<model_name>_list.html
    # queryset = Product.objects.all()
    template_name = 'product_details.html'
    
    def get_object(self):
        obj_id = self.kwargs.get('id')
        return get_object_or_404(Product, id=obj_id)

class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = '/product/list'

    def form_valid(self, form):
        return super().form_valid(form)

def product_list_view(request):
    products = Product.objects.all()
    context = {}
    context['products'] = products
    return render(request, 'home.html', context)


def product_details_view(request, id):
    product = Product.objects.get(id=id)
    context = {}
    context['product'] = product
    return render(request, 'product_details.html', context)

def product_create(request):
    form = ProductForm()

    if request.method == 'POST':
        my_form = ProductForm(request.POST or None)
        if my_form.is_valid():
            form_data = my_form.cleaned_data
            print(form_data)
            new_product = Product.objects.create(**form_data)

    context = {
        'form': form
    }
    return render(request, 'product_create.html', context)