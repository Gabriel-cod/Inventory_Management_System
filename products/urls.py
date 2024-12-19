from django.urls import path
from .views import ProductsListView, ProductsCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('products/list/', ProductsListView.as_view(), name='products_list'),
    path('products/create/', ProductsCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/details/', ProductDetailView.as_view(), name='product_details'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
