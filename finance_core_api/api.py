from rest_framework.decorators import action
from rest_framework.response import Response

from account.transaction import ResourceTransaction
from finance_core_api.models import Account, Resource, Transaction
from rest_framework import viewsets
from .serializers import AccountSerializer, ResourceSerializer, TransactionSerializer
from account.resource import Account as MyAccount, Resource as MyResource
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

    def create(self, request, *args, **kwargs):
        body = request.body.decode('utf-8')
        body_str = json.loads(body)
        persistence = Resource.objects.create(name=body_str['name'], total_amount=body_str['total_amount'],
                                              remain_amount=body_str['remain_amount'])
        res = ResourceSerializer(persistence, many=False)
        return Response(res.data, status=201)

    @action(methods=['GET', 'DELETE', 'POST'], detail=True)
    def related_accounts(self, request, pk, *args, **kwargs):
        if request.method == 'GET':
            return self.get_related_account(pk)
        elif request.method == 'DELETE':
            return self.delete_account(request, pk, args, kwargs)
        elif request.method == 'POST':
            return self.create_related_account(request, pk)

    @staticmethod
    def get_related_account(pk):
        account_qs = Account.objects.filter(fk_resource_id=pk)
        account = AccountSerializer(account_qs, many=True)
        return Response(account.data, status=200)

    @staticmethod
    def delete_account(request, pk, *args, **kwargs):
        account_id = request.GET['account_id']
        if not isinstance(int(account_id), int):
            return Response(data="Incorrect format for account_id", status=400)
        else:
            try:
                """Load up from db"""
                resource_qs = Resource.objects.filter(id=pk)
                related_account_qs = Account.objects.filter(fk_resource_id=pk, id=account_id)
                resource = resource_qs.first()
                resource_account = related_account_qs.first()

                """Execute the logic"""
                # TODO: Use Transaction object to execute remove account . Update the resource with remain amount
                #  Need some kind of log on action
                domain_source = MyResource(name=resource.name, amount=resource.remain_amount)
                my_acc = MyAccount(name=resource_account.name, from_resource=domain_source)

                my_acc.amount = resource_account.remain_amount
                my_acc.return_to_resource()

                """Update values"""
                resource_qs.update(remain_amount=domain_source.get_current_amount())
                instance = related_account_qs.get(id=account_id)
                instance.delete()

                return Response(status=200)
            except Exception as e:
                print(e)
                return Response(data="Account not found", status=500)

    @staticmethod
    def create_related_account(request, pk):
        data = json.loads(request.body.decode('utf-8'))

        """Loading from db"""
        resource_queryset = Resource.objects.filter(id__exact=pk)
        resource_persisted_model = resource_queryset.first()

        """Hanlde logic"""
        acc_name = data['account_name']
        account_amount = data['account_amount']

        # TODO: Use Transaction object to execute create new account. Then save the transaction to Transaction table

        domain_resource = MyResource(name=resource_persisted_model.name,
                                     amount=resource_persisted_model.remain_amount)
        domain_account = MyAccount(name=acc_name, amount=0, from_resource=domain_resource)
        create_transaction = ResourceTransaction(date_of_execution=None, from_resource=domain_resource,
                                                 to_resource=domain_account)
        create_transaction.execute_deposit(Decimal(account_amount))

        resource_queryset.update(remain_amount=domain_resource.get_current_amount())
        new_account = Account.objects.create(name=domain_account.get_name(),
                                             total_amount=domain_account.get_current_amount(),
                                             remain_amount=domain_account.get_current_amount(), fk_resource_id=pk)

        Transaction.objects.create(type="WITHDRAW", date_of_execution=create_transaction.get_date(),
                                   description=create_transaction.get_name(), fk_account_id=new_account.id)
        """Serialize into response"""
        new_account = AccountSerializer(new_account, many=False)
        return Response(data=new_account.data, status=201)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = []
