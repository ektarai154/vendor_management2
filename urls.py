# vendors/urls.py
from django.urls import path
from .views import VendorListCreateView, ProductListCreateView

urlpatterns = [
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    # Add other paths as needed
]
