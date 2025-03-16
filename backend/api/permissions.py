from rest_framework import permissions


class PublicOrAuthenticatedReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            (request.method in permissions.SAFE_METHODS
             and (request.user.is_anonymous
                  or request.user.is_authenticated))
            or request.user.is_superuser
            or request.user.is_staff
        )


class CreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.creator == request.user
        )
