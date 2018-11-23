from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.api import UserCreateView, UserDetailView, UserListApiView
from users.views import LoginView, UserListView, LogoutView, RegisterView

router = DefaultRouter()
router.register('users', UserCreateView, basename='users')
router.register('users', UserDetailView, basename='users')
router.register('blogs', UserListApiView, basename='blogs')

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('blogs', UserListView.as_view(), name='user_list'),
    path('api/1.0/', include(router.urls), name='user_api'),
]
