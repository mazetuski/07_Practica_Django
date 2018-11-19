from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView

from blog.forms import PostForm
from blog.models import Post


class HomeView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/home.html'
    ordering = ['-pub_date']


@method_decorator(login_required, name='dispatch')
class NewPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/new_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
