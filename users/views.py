from django.contrib import messages
from django.contrib.auth import \
    authenticate, \
    login as login_user_in_django, \
    logout as logout_user_in_django
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from users.forms import RegisterForm


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


class LogoutView(View):

    def get(self, request):
        logout_user_in_django(request)
        messages.success(request, 'You have been logout successfully!')
        return redirect('home')


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/register.html', {'form': form})
        # Create new user, authenticate it and redirect to home
        new_user = User()
        new_user.username = form.cleaned_data.get('username')
        new_user.first_name = form.cleaned_data.get('first_name')
        new_user.last_name = form.cleaned_data.get('last_name')
        new_user.set_password(form.cleaned_data.get('password'))
        new_user.email = form.cleaned_data.get('email')
        new_user.save()
        messages.success(request, 'Register successfully')
        login_user_in_django(request, new_user)
        return redirect('home')


class UserListView(ListView):
    model = User
    queryset = User.objects.all()
    paginate_by = 10
    template_name = 'users/users.html'
