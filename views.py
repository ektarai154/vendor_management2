from django.shortcuts import render

# Create your views here.
# vendors/views.py
from rest_framework import generics
from .models import Vendor, Product
from .serializers import VendorSerializer, ProductSerializer

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
