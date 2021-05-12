from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category
from categories.serializers import CategorySerializer
from .permissions import IsCategoryUserOrReadOnly
from rest_framework.permissions import IsAuthenticated

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsCategoryUserOrReadOnly, IsAuthenticated)