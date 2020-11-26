from rest_framework import serializers
from finance_core_api.models import Account


class AccountSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        Account.objects.create(validated_data)

    class Meta:
        model = Account
        fields = '__all__'
