from django.urls import path

from blog.views import HomeView, NewPostView, BlogView, PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('new-post', NewPostView.as_view(), name='new_post'),
    path('blogs/<pk>', BlogView.as_view(), name='blog'),
    path('blogs/<username>/<int:pk>', PostDetailView.as_view(), name='post_detail')
]
