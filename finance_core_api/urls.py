from rest_framework import routers
from .api import AccountViewSet, ResourceViewSet

router = routers.DefaultRouter()
router.register('api/accounts', AccountViewSet, 'accounts')
router.register('api/resources', ResourceViewSet, 'resources')

urlpatterns = router.urls
