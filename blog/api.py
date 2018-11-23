from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from blog.models import Post
from blog.serializers import PostSerializer


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
