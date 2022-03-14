# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'billinginfo', views.BillingInfoViewSet)
router.register(r'medicalhistory', views.MedicalHistoryViewSet)
router.register(r'roles', views.RolesViewSet)
router.register(r'userroles', views.UserRolesViewSet)
router.register(r'measurements', views.MeasurementsViewSet)
router.register(r'device', views.DeviceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]