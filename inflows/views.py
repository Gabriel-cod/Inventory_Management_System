from django.views import generic
from django.urls import reverse_lazy
from core.metrics import get_sales_metrics
from .models import Inflow
from .forms import InflowForm


class InflowListView(generic.ListView):
    model = Inflow
    template_name = 'inflows_list.html'
    context_object_name = 'inflows'

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


class InflowCreateView(generic.CreateView):
    model = Inflow
    template_name = 'inflows_register.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflows_list')


class InflowDetailView(generic.DetailView):
    model = Inflow
    template_name = 'inflow_details.html'
    context_object_name = 'inflow'
