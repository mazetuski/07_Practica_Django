from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.api import PostListViewSet, PostViewSet
from blog.views import HomeView, NewPostView, BlogView, PostDetailView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('new-post', NewPostView.as_view(), name='new_post'),
    path('blogs/<pk>', BlogView.as_view(), name='blog'),
    path('blogs/<username>/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('api/1.0/', include(router.urls), name='post_api'),
    path('api/1.0/blog/<int:user>/', PostListViewSet.as_view({'get': 'list'}), name='post_list_api')
]
