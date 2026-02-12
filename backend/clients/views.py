from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Client, ClientUnit, DepartmentContact
from .serializers import ( ClientSerializer, ClientUnitSerializer, DepartmentContactSerializer,)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.prefetch_related("units").all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_value_regex = r'\d+'

    def destroy(self, request, *args, **kwargs):
        """
        Deletes client and all related units automatically (CASCADE).
        """
        return super().destroy(request, *args, **kwargs)

class ClientUnitViewSet(viewsets.ModelViewSet):
    queryset = ClientUnit.objects.select_related(
        "client",
        "accounts_officer",
        "operation_department",
    ).all()
    serializer_class = ClientUnitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        client_id = request.data.get("client")

        if not client_id:
            return Response(
                {"client": "Client ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(client_id=client_id)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class DepartmentContactViewSet(viewsets.ModelViewSet):
    queryset = DepartmentContact.objects.all()
    serializer_class = DepartmentContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
