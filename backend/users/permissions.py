"""
Custom Permissions for User Management
"""
from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permission to only allow owners of an object or Admin to edit it
    """
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # Admin can access any user
        if request.user.is_superuser or request.user.is_staff:
            return True
        
        # Users can only access their own profile
        return obj == request.user


class IsAdmin(permissions.BasePermission):
    """
    Permission to only allow Admin users (superuser or staff)
    """
    
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            (request.user.is_superuser or request.user.is_staff)
        )