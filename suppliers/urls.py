from django.urls import path
from .views import SuppliersListView, SuppliersCreateView, SupplierUpdateView, SupplierDeleteView, SupplierDetailView

urlpatterns = [
    path('suppliers/list/', SuppliersListView.as_view(), name='suppliers_list'),
    path('suppliers/create/', SuppliersCreateView.as_view(), name='suppliers_create'),
    path('suppliers/<int:pk>/details/', SupplierDetailView.as_view(), name='supplier_details'),
    path('suppliers/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),
]
