from rest_framework.permissions import BasePermission


class UserPermissions(BasePermission):
    # TODO: CAMBIAR ESTO
    def has_permission(self, request, view):
        # El usuario auth puede realizar la acción general
        return request.user.is_authenticated \
               or view.action in ['retrieve', 'list']

    def has_object_permission(self, request, view, obj):
        # El usuario auth puede realizar la acción sobre el objeto obj
        return view.action == 'retrieve' \
               or obj == request.user \
               or request.user.is_superuser