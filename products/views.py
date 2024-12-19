from django.views import generic
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm
from brands.models import Brand
from categories.models import Category
from core.metrics import get_products_metrics


class ProductsListView(generic.ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        brand = self.request.GET.get('brand')
        category = self.request.GET.get('category')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if brand and brand != 'Brand':
            queryset = queryset.filter(brand__name=brand)
        if category and category != 'Category':
            queryset = queryset.filter(category__name=category)

        return queryset

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['brands'] = Brand.objects.all()
        data['categories'] = Category.objects.all()
        data['products_metrics'] = get_products_metrics()
        return data


class ProductsCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products_create.html'
    success_url = reverse_lazy('products_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Create Product'
        data['post_url'] = 'products_create'
        return data


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products_create.html'

    def get_success_url(self):
        product_id = self.get_object().pk
        return reverse_lazy('product_details', kwargs={'pk': product_id})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Update Product'
        data['post_url'] = 'product_update'
        data['product_id'] = self.get_object().pk
        return data


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('products_list')

    def get(self, request, *args, **kwargs):
        product_title = self.get_object().title
        if product_title:
            return redirect(reverse('products_list') + f'?title={product_title}')
        raise Http404()
