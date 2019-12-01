from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    """Checks if the user has admin priviledges or by default has read only capabilities"""

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin


class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    """Checks if the logged user is the author of the review"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.review_author == request.user
