from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post


class HomeView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/home.html'
