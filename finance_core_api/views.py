from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from finance_core_api.models import Account


def main_view(request, *args, **kwargs):
    queryset = Account.objects.all()
    return HttpResponse(queryset, content_type="application/json")
