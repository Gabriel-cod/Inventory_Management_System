from django.urls import path
from .views import OutflowListView, OutflowCreateView, OutflowDetailView

urlpatterns = [
    path('outflows/list/', OutflowListView.as_view(), name='outflows_list'),
    path('outflows/register/', OutflowCreateView.as_view(), name='outflows_register'),
    path('outflows/<int:pk>/details/', OutflowDetailView.as_view(), name='outflow_details'),
]
