from django.contrib import messages
from django.contrib.auth import \
    authenticate, \
    login as login_user_in_django, \
    logout as logout_user_in_django
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView


class LoginView(View):

    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user_in_django(request, user)
            redirect_url = request.GET.get('next', 'home')
            return redirect(redirect_url)
        messages.error(request, 'Wrong username or password')
        return render(request, 'users/login.html')


class UserListView(ListView):
    model = User
    queryset = User.objects.all().order_by('-post__pub_date')
    paginate_by = 10
    template_name = 'users/users.html'
