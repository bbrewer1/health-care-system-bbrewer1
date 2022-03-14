# serializers.py
from rest_framework import serializers

from .models import User, BillingInfo, MedicalHistory, Roles, UserRoles, Measurements, Device

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('uid', 'birth_date', 'address', 'pcp', 'sex', 'emergency_contacts')

class BillingInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BillingInfo
        fields = ('uid', 'insurance_company', 'member_id', 'member_name', 'saved_credit_cards', 'billing_address')

class MedicalHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = ('uid', 'current_medications', 'family_medical_history', 'past_medications', 'allergies', 'medical_history')

class RolesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Roles
        fields = ('uid', 'role')

class UserRolesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRoles
        fields = ('uid', 'rid', 'delete', 'time')

class MeasurementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurements
        fields = ('uid', 'temperature', 'blood_pressure', 'pulse', 'blood_oxygen', 'weight', 'height')

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('uid', 'type', 'date_of_purchase', 'mac', 'user_title', 'firmware_version', 'software_version')


