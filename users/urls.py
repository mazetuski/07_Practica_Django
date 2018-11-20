from django.urls import path

from users.views import LoginView, UserListView, LogoutView, RegisterView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('blogs', UserListView.as_view(), name='user_list')
]