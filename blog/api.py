from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from blog.models import Post
from blog.permissions import BlogPermissions
from blog.serializers import PostListSerializer, PostSerializer


class PostListViewSet(ListAPIView, GenericViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostListSerializer
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description_short']
    filter_fields = ['category']
    ordering = ['title', 'pub_date']

    def get_queryset(self):
        user_post = self.kwargs['user']
        user_logged = self.request.user
        if user_logged.is_authenticated and (user_logged.is_superuser or user_logged == user_post):
            return Post.objects.filter(owner=user_post)
        return Post.objects.filter(owner=user_post, pub_date__lte=datetime.now())


class PostViewSet(CreateAPIView, RetrieveUpdateDestroyAPIView, GenericViewSet):

    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, BlogPermissions]
    serializer_class = PostSerializer
