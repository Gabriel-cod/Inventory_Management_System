from django.urls import path
from .views import BrandsListView, BrandsCreateView, BrandsDeleteView, \
    BrandsUpdateView, BrandDetailView

urlpatterns = [
    path('brands/list/', BrandsListView.as_view(), name='brands_list'),
    path('brands/create/', BrandsCreateView.as_view(), name='brands_create'),
    path('brands/<int:pk>/details/', BrandDetailView.as_view(), name='brand_details'),
    path('brands/<int:pk>/delete/', BrandsDeleteView.as_view(), name='brand_delete'),
    path('brands/<int:pk>/update/', BrandsUpdateView.as_view(), name='brand_update'),
]
