from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryDetailView, CategoryDeleteView, CategoryUpdateView

urlpatterns = [
    path('categories/list/', CategoryListView.as_view(), name='categories_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='categories_create'),
    path('categories/<int:pk>/details/', CategoryDetailView.as_view(), name='category_details'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update')
]
