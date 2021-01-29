"""Custom permissions for api app."""
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Permission check for company owner.
       Return True if current user is company owner, else - False.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
