from rest_framework.response import Response

from finance_core_api.models import Account, Resource
from rest_framework import viewsets
from .serializers import AccountSerializer, ResourceSerializer
from account.resource import Account as MyAccount, IncomeSource
import json
from decimal import Decimal


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
        print("ISHTIS")
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

    def create_related_account(self, request, pk):
        data = json.loads(request.body.decode('utf-8'))
        resource_queryset = Resource.objects.filter(id__exact=pk)
        resource_persisted_model = resource_queryset.first()
        my_resource = IncomeSource(name=resource_persisted_model.name,
                                   amount=resource_persisted_model.total_amount)
        account = MyAccount(name=data['account_name'], from_resource=my_resource)
        account.withdraw_from_resource(Decimal(data['account_amount']))

        resource_queryset.update(total_amount=my_resource.amount)
        created_account = Account.objects.create(name=account.name, current_amount=account.get_remain_in_account,
                                                 remain_amount=account.get_remain_in_account, fk_resource_id=pk)

        new_account = AccountSerializer(source=created_account, many=False)
        return Response(data=new_account.data, status=201)
