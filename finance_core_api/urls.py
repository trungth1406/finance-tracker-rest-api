from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .api import AccountViewSet, ResourceViewSet, ResourceAccountViewSet

accounts_list = AccountViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

resource_list = ResourceViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

resource_accounts_list = ResourceAccountViewSet.as_view({
    'get': 'get_related_accounts',
    'delete': 'delete_account'
})

urlpatterns = [
    path('accounts/', accounts_list, name='accounts'),
    path('resources/', resource_list, name='resources'),
    path('resources/<int:pk>/related-accounts/', resource_accounts_list, name='get_related_accounts'),
    path(r'^resources/<int:pk>/related-accounts/(?P<account_id>=[0-9]+)/$', resource_accounts_list,
         name='delete-related-accounts'),
]
