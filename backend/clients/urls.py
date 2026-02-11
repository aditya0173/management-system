from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ClientUnitViewSet, DepartmentContactViewSet

router = DefaultRouter()
router.register("clients", ClientViewSet)
router.register("clients/units", ClientUnitViewSet)
router.register("clients/contacts", DepartmentContactViewSet)

urlpatterns = router.urls
