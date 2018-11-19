from django.urls import path

from users.views import LoginView, UserListView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('blogs', UserListView.as_view(), name='user_list')
]