from django.views import generic
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.http import Http404
from .models import Supplier
from .forms import SupplierForm


class SuppliersListView(generic.ListView):
    model = Supplier
    template_name = 'suppliers_list.html'
    context_object_name = 'suppliers'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__contains=name)

        return queryset


class SuppliersCreateView(generic.CreateView):
    model = Supplier
    template_name = 'suppliers_create.html'
    form_class = SupplierForm
    success_url = reverse_lazy('suppliers_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Create Supplier'
        data['post_url'] = 'suppliers_create'
        return data


class SupplierDetailView(generic.DetailView):
    model = Supplier
    template_name = 'supplier_details.html'
    context_object_name = 'supplier'


class SupplierUpdateView(generic.UpdateView):
    model = Supplier
    template_name = 'suppliers_create.html'
    form_class = SupplierForm

    def get_success_url(self):
        supplier_id = self.get_object().pk
        return reverse_lazy('supplier_details', kwargs={'pk': supplier_id})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Update Supplier'
        data['post_url'] = 'supplier_update'
        data['supplier_id'] = self.get_object().pk
        return data


class SupplierDeleteView(generic.DeleteView):
    model = Supplier
    success_url = reverse_lazy('suppliers_list')

    def get(self, request, *args, **kwargs):
        supplier_name = self.get_object().name
        if supplier_name:
            return redirect(reverse('suppliers_list') + f'?name={supplier_name}')
        raise Http404()
