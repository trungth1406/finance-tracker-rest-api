from pprint import pprint

from rest_framework.routers import Route, SimpleRouter, DynamicRoute

from .api import AccountViewSet, ResourceViewSet, TransactionViewSet


class MyRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list', 'post': 'create'},
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
        ),
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}?(?P<current_account>)$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        )
    ]


route = MyRouter()
route.register('accounts', AccountViewSet)
route.register('resources', ResourceViewSet)
route.register('transactions', TransactionViewSet)
urlpatterns = route.urls
pprint(route.urls)
