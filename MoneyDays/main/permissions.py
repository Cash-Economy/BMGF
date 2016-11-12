from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            return False
        if request.user.is_staff:
            return True
        if view.kwargs.get('pk_user') == "self":
            return True
        user_id = str(request.user.id)
        if user_id == view.kwargs.get('pk_user'):
            return True

        return False


class NotAllowRegisterAccountToAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        print("NotAllowRegisterAccountToAuthenticated")
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.user.is_authenticated():
                raise PermissionDenied(detail="The user is already logged in, first log out, to create a new account")
            else:
                return True
