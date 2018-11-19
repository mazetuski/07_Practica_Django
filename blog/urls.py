from django.urls import path

from blog.views import HomeView, NewPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('new-post', NewPostView.as_view(), name='new_post')
]
