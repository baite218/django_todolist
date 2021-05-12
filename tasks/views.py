from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework.viewsets import ModelViewSet
from .permissions import IsTaskUserOrReadOnly

class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'
    permission_classes = (IsTaskUserOrReadOnly, )