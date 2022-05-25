from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Address
from .serializer import AddressSeriazer
# Create your views here.
class AddressViewSet (ModelViewSet):
    serializer_class = AddressSeriazer
    queryset = Address.objects.all()