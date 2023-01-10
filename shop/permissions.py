from rest_framework import permissions


class IsSenderPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or
                    request.user.profile.is_sender)