from rest_framework import serializers
from finance_core_api.models import Account, Resource, Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['fk_resource']


class ResourceSerializer(serializers.ModelSerializer):
    total_accounts = serializers.SerializerMethodField('get_total_accounts')

    class Meta:
        model = Resource
        fields = "__all__"

    @staticmethod
    def get_total_accounts(instance):
        account_query_set = Account.objects.filter(fk_resource_id=instance.id)
        total_account = account_query_set.count()
        return total_account


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
