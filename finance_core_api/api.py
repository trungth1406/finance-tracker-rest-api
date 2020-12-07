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


class ResourceAccountViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = []

    def get_related_accounts(self, request, pk):
        result = Account.objects.filter(fk_resource_id=pk)
        accounts = AccountSerializer(result, many=True)
        return Response(accounts.data)

    def delete_account(self, request, *args, **kwargs):
        account_id = request.GET['account_id']
        if not isinstance(int(account_id), int):
            return Response(data="Incorrect format for account_id", status=400)
        else:
            try:
                resource_account = Account.objects.filter(fk_resource_id=kwargs['pk'])
                instance = resource_account.get(id__exact=account_id)
                instance.delete()
                return Response()
            except:
                return Response(data="Account not found", status=500)

