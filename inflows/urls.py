from django.urls import path
from .views import InflowListView, InflowCreateView, InflowDetailView

urlpatterns = [
    path('inflows/list/', InflowListView.as_view(), name='inflows_list'),
    path('inflows/register/', InflowCreateView.as_view(), name='inflows_register'),
    path('inflows/<int:pk>/details/', InflowDetailView.as_view(), name='inflow_details'),
]
