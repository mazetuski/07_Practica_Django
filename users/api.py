from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.viewsets import GenericViewSet

from users.permissions import UserPermissions
from users.serializers import UserSerializer, UserListSerializer


class UserCreateView(CreateAPIView, GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView, GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]


class UserListApiView(ListAPIView, GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['first_name', 'last_name']
    ordering = ['first_name', 'last_name']
