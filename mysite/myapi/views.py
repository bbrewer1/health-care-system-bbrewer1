from django.shortcuts import render

from rest_framework import viewsets

from .serializers import UserSerializer, BillingInfoSerializer, MedicalHistorySerializer, RolesSerializer, UserRolesSerializer, MeasurementsSerializer, DeviceSerializer
from .models import User, BillingInfo, MedicalHistory, Roles, UserRoles, Measurements, Device

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('uid')
    serializer_class = UserSerializer

class BillingInfoViewSet(viewsets.ModelViewSet):
    queryset = BillingInfo.objects.all().order_by('uid')
    serializer_class = BillingInfoSerializer

class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedicalHistory.objects.all().order_by('uid')
    serialzer_class = MedicalHistorySerializer

class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all().order_by('uid')
    serialzer_class = RolesSerializer

class UserRolesViewSet(viewsets.ModelViewSet):
    queryset = UserRoles.objects.all().order_by('uid')
    serialzer_class = UserRolesSerializer

class MeasurementsViewSet(viewsets.ModelViewSet):
    queryset = Measurements.objects.all().order_by('uid')
    serialzer_class = MeasurementsSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('uid')
    serialzer_class = DeviceSerializer