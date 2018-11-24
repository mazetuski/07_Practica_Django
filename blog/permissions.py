from datetime import datetime

from django.utils import timezone
from rest_framework.permissions import BasePermission


class BlogPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated \
               or view.action == 'retrieve'

    def has_object_permission(self, request, view, obj):
        return (view.action == 'retrieve' and obj.pub_date < timezone.now()) \
               or obj.owner == request.user \
               or request.user.is_superuser
