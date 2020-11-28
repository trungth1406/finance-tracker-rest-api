from finance_core_api.models import Account, Resource
from rest_framework import viewsets, permissions
from .serializers import AccountSerializer, ResourceSerializer


# Viewset
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = []


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = []
