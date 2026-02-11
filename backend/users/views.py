"""
Views for User Management
"""
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import User
from .serializers import (
    UserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    UserDetailSerializer,
    ChangePasswordSerializer
)
from .permissions import IsOwnerOrAdmin, IsAdmin


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User CRUD operations
    
    list: Get all users (Admin only)
    create: Create new user (Anyone can register)
    retrieve: Get user details
    update: Update user details
    partial_update: Partially update user
    destroy: Delete user (Admin only)
    """
    
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'is_active': ['exact'],
        'is_staff': ['exact'],
        'is_superuser': ['exact'],
        'created_at': ['gte', 'lte'],
    }
    search_fields = ['name', 'email']
    ordering_fields = ['created_at', 'name', 'email']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action"""
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        elif self.action == 'retrieve':
            return UserDetailSerializer
        return UserSerializer
    
    def get_permissions(self):
        """Return appropriate permissions based on action"""
        if self.action == 'create':
            return [AllowAny()]  # Anyone can register
        elif self.action in ['update', 'partial_update']:
            return [IsOwnerOrAdmin()]
        elif self.action == 'destroy':
            return [IsAdmin()]
        return [IsAuthenticated()]
    
    @swagger_auto_schema(
        operation_description="Get list of all users (Admin only)",
        responses={200: UserSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        """List all users"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Register a new user",
        request_body=UserCreateSerializer,
        responses={
            201: UserSerializer,
            400: "Bad Request"
        }
    )
    def create(self, request, *args, **kwargs):
        """Create a new user"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Return user details
        response_serializer = UserSerializer(user)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(
        operation_description="Get user profile",
        responses={200: UserDetailSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        """Get user details"""
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Update user details",
        request_body=UserUpdateSerializer,
        responses={200: UserSerializer}
    )
    def update(self, request, *args, **kwargs):
        """Update user"""
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Partially update user details",
        request_body=UserUpdateSerializer,
        responses={200: UserSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        """Partially update user"""
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Delete user (Admin only)",
        responses={204: "User deleted successfully"}
    )
    def destroy(self, request, *args, **kwargs):
        """Delete user"""
        return super().destroy(request, *args, **kwargs)
    
    @swagger_auto_schema(
        method='get',
        operation_description="Get current user profile",
        responses={200: UserDetailSerializer}
    )
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Get current authenticated user profile"""
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        method='post',
        operation_description="Change user password",
        request_body=ChangePasswordSerializer,
        responses={
            200: "Password changed successfully",
            400: "Bad Request"
        }
    )
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def change_password(self, request):
        """Change password for current user"""
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            # Set new password
            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()
            
            return Response({
                'message': 'Password changed successfully'
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        method='get',
        operation_description="Get user statistics",
        responses={200: openapi.Response('Statistics', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'total_users': openapi.Schema(type=openapi.TYPE_INTEGER),
                'active_users': openapi.Schema(type=openapi.TYPE_INTEGER),
                'staff_users': openapi.Schema(type=openapi.TYPE_INTEGER),
                'superusers': openapi.Schema(type=openapi.TYPE_INTEGER),
            }
        ))}
    )
    @action(detail=False, methods=['get'], permission_classes=[IsAdmin])
    def statistics(self, request):
        """Get user statistics"""
        total_users = User.objects.count()
        active_users = User.objects.filter(is_active=True).count()
        staff_users = User.objects.filter(is_staff=True).count()
        superusers = User.objects.filter(is_superuser=True).count()
        
        return Response({
            'total_users': total_users,
            'active_users': active_users,
            'staff_users': staff_users,
            'superusers': superusers,
        })