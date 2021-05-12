from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializers import UserSerializer
from .permissions import IsOwnerUserOrReadOnly

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerUserOrReadOnly, )
