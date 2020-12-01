from caching.jsondb import ModelSerializer
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(methods=['get'], detail=True, url_path="related-accounts")
    def get_related_accounts(self, request, pk):
        result = Account.objects.filter(fk_resource_id=pk)
        accounts = AccountSerializer(result, many=True)
        return Response(accounts.data)
