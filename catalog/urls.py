from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductDetailView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, UnpublishProductView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('unpublish/<int:pk>/', UnpublishProductView.as_view(), name='product_unpublish'),
    path('create/new/', ProductCreateView.as_view(), name='product_create'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]
