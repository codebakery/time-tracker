from rest_framework import permissions
from .models import Record


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Record):
        return obj.user == request.user
