from django.urls import path

from users.views import LoginView

urlPatterns = {
    path('login', LoginView.as_view(), name='login')
}