from django.views import generic
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.http.response import Http404
from .models import Category
from .forms import CategoryForm


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class CategoryCreateView(generic.CreateView):
    model = Category
    template_name = 'categories_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categories_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['post_url'] = 'categories_create'
        data['title'] = 'Create Category'
        return data


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'category_details.html'
    context_object_name = 'category'


class CategoryDeleteView(generic.DeleteView):
    model = Category
    success_url = reverse_lazy('categories_list')

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        category_name = self.get_object().name
        if category_name:
            return redirect(reverse('categories_list') + f'?name={category_name}')
        raise Http404()


class CategoryUpdateView(generic.UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories_create.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Update Category'
        data['post_url'] = 'category_update'
        data['category_id'] = self.get_object().pk
        return data

    def get_success_url(self):
        category_id = self.get_object().pk
        return reverse_lazy('category_details', kwargs={'pk': category_id})
