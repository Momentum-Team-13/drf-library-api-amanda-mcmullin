from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission allows ONLY owner of an object editing rights
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
