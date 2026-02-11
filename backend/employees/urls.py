from rest_framework.routers import DefaultRouter
from .views import EmployeesViewset

router = DefaultRouter()
router.register("employee", EmployeesViewset)

urlpatterns = router.urls