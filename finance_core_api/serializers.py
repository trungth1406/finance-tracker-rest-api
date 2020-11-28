from rest_framework import serializers
from finance_core_api.models import Account, Resource


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['id']


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        exclude = ['id']
