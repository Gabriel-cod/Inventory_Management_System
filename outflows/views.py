from django.views import generic
from django.urls import reverse_lazy
from core.metrics import get_sales_metrics
from .models import Outflow
from .forms import OutflowForm


class OutflowListView(generic.ListView):
    model = Outflow
    template_name = 'outflows_list.html'
    context_object_name = 'outflows'

    def get_queryset(self):
        queryset = super().get_queryset()
        product_title = self.request.GET.get('product')
        if product_title:
            queryset = queryset.filter(product__title__contains=product_title)

        return queryset

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['sales_metrics'] = get_sales_metrics()
        return data


class OutflowCreateView(generic.CreateView):
    model = Outflow
    template_name = 'outflows_register.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflows_list')


class OutflowDetailView(generic.DetailView):
    model = Outflow
    template_name = 'outflow_details.html'
    context_object_name = 'outflow'
