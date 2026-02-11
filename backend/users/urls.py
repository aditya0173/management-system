"""
URL Configuration for Users App
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

app_name = 'users'

# Create router and register viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]

# Available endpoints:
# GET    /api/users/              - List all users (Admin only)
# POST   /api/users/              - Register new user (Anyone can register)
# GET    /api/users/{id}/         - Get user details (Authenticated)
# PUT    /api/users/{id}/         - Update user (Owner or Admin)
# PATCH  /api/users/{id}/         - Partial update user (Owner or Admin)
# DELETE /api/users/{id}/         - Delete user (Admin only)
# GET    /api/users/me/           - Get current user profile (Authenticated)
# POST   /api/users/change_password/ - Change password (Authenticated)
# GET    /api/users/statistics/   - Get user statistics (Admin only)