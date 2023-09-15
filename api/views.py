from django.shortcuts import render
from rest_framework.generics import GenericAPIView,RetrieveUpdateDestroyAPIView
from main.serializers import *
from main.models import *

class CategoryCreateListView(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()