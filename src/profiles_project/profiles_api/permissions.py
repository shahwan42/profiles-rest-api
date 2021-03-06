from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profiles."""

        # allow anybody to read (make GET,HEAD,OPTIONS requests)
        if request.method in permissions.SAFE_METHODS:
            return True
        # allow owner only to edit
        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their status."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying ty update his own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
