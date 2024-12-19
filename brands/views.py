from django.views import generic
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.http import Http404
from .models import Brand
from .forms import BrandForm


class BrandsListView(generic.ListView):
    model = Brand
    template_name = 'brands_list.html'
    context_object_name = 'brands'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class BrandsCreateView(generic.CreateView):
    model = Brand
    template_name = 'brands_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brands_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Create Brand'
        data['post_url'] = 'brands_create'
        return data


class BrandDetailView(generic.DetailView):
    model = Brand
    template_name = 'brand_details.html'
    context_object_name = 'brand'


class BrandsDeleteView(generic.DeleteView):
    model = Brand
    success_url = reverse_lazy('brands_list')

    def get(self, request, *args, **kwargs):
        brand_name = self.get_object().name
        if brand_name:
            return redirect(reverse('brands_list') + f'?name={brand_name}')
        raise Http404()


class BrandsUpdateView(generic.UpdateView):
    model = Brand
    template_name = 'brands_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brands_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Update Brand'
        data['post_url'] = 'brand_update'
        data['brand_id'] = self.get_object().pk
        return data

    def get_success_url(self):
        brand_id = self.get_object().pk
        return reverse_lazy('brand_details', kwargs={'pk': brand_id})
