"""
URL configuration for management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# ========================================
# Swagger/OpenAPI Schema Configuration
# ========================================
schema_view = get_schema_view(
    openapi.Info(
        title="Management System API",
        default_version='v1',
        description="""
# Management System API Documentation

Welcome to the Management System API. This API provides endpoints for user management and authentication.

## Authentication

This API uses JWT (JSON Web Token) authentication. To use protected endpoints:

1. **Register**: POST to `/api/users/` with your details
2. **Login**: POST to `/api/token/` with email and password to get tokens
3. **Use Token**: Include in header: `Authorization: Bearer <access_token>`
4. **Refresh**: POST to `/api/token/refresh/` with refresh token when access token expires

## Available Features

- User Registration and Management
- JWT Authentication (Login/Logout)
- User Profile Management
- Password Change
- Admin User Statistics

## Response Format

All responses are in JSON format with appropriate HTTP status codes.

### Success Response
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
}
```

### Error Response
```json
{
    "detail": "Error message here"
}
```
        """,
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="support@yourapp.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


# ========================================
# URL Patterns
# ========================================
urlpatterns = [
    # ========================================
    # Django Admin Panel
    # ========================================
    path("admin/", admin.site.urls, name='admin'),
    
    # ========================================
    # JWT Authentication Endpoints
    # ========================================
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    
    # ========================================
    # API Documentation (Swagger/ReDoc)
    # ========================================
    # Swagger UI - Interactive API documentation
    path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-alt'),
    
    # ReDoc UI - Alternative API documentation
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # API Schema Downloads
    path("swagger.json/", schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("swagger.yaml/", schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
    
    # ========================================
    # Application API Endpoints
    # ========================================
    # User Management API
    path("api/", include("users.urls")),  # Replace 'users' with your app name if different
    path("api/", include("clients.urls")),  # Replace 'users' with your app name if different
    path("api/", include("employees.urls")),  # Replace 'users' with your app name if different
    
    # Add more app URLs here as needed
    # path("api/", include("another_app.urls")),
]


# ========================================
# Serve Media and Static Files in Development
# ========================================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# ========================================
# Custom Error Handlers (Optional)
# ========================================
# handler404 = 'your_app.views.custom_404'
# handler500 = 'your_app.views.custom_500'
# handler403 = 'your_app.views.custom_403'
# handler400 = 'your_app.views.custom_400'