from rest_framework import permissions

from .models import User

class IsSameUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: User):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj == request.user
