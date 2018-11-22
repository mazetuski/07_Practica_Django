from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.viewsets import GenericViewSet

from users.permissions import UserPermissions
from users.serializers import UserSerializer


class UserViewSet(CreateAPIView, RetrieveUpdateDestroyAPIView, GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]
