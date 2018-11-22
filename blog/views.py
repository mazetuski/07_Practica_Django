from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView

from blog.forms import PostForm
from blog.models import Post


class HomeView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/home.html'

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=datetime.now()).order_by('-pub_date')

class BlogView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/blog.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['pk'])
        return Post.objects.filter(pub_date__lte=datetime.now(), owner=user).order_by('-pub_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.filter(pub_date__lte=datetime.now(), owner=user, pk=self.kwargs['pk'])


@method_decorator(login_required, name='dispatch')
class NewPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/new_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
