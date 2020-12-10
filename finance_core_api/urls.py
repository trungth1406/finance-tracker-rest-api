from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import Route, SimpleRouter, DynamicRoute

from .api import AccountViewSet, ResourceViewSet, ResourceAccountViewSet


class MyRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        )
    ]


route = MyRouter()
route.register('accounts', AccountViewSet)
route.register('resources', ResourceViewSet)
urlpatterns = route.urls
# resource_list = ResourceViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# accounts_list = AccountViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# resource_accounts_list = ResourceAccountViewSet.as_view({
#     'get': 'get_related_accounts',
#     'post': 'create_related_account',
#     'delete': 'delete_account'
# })

# urlpatterns = [
#
#     path('accounts/', accounts_list, name='accounts'),
#     path('resources/', resource_list, name='resources'),
#     path(r'resources/<int:pk>/', resource_list, name='resource_detail'),
#     path('resources/<int:pk>/related-accounts/', resource_accounts_list, name='get_related_accounts'),
#     path(r'^resources/<int:pk>/related-accounts/(?P<account_id>=[0-9]+)/$', resource_accounts_list,
#          name='delete-related-accounts'),
#     path('resources/<int:pk>/related-accounts/', resource_accounts_list, name='create-related-account')
# ]
