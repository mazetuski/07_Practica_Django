from rest_framework.permissions import BasePermission

# Only an admin and the user can see the details ot this user, update his info
# or remove it, anonymous people can register in the app
class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated \
               or view.action == 'create'

    def has_object_permission(self, request, view, obj):
        return obj == request.user \
               or request.user.is_superuser