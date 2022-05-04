# serializers.py
from rest_framework import serializers

from .models import User, BillingInfo, MedicalHistory, Roles, UserRoles, Measurements, Device

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'address', 'pcp', 'sexes', 'sex', 'emergency_contacts')

class BillingInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BillingInfo
        fields = ('user', 'insurance_company', 'member_id', 'member_name', 'payment_card_number', 'payment_card_expiration', 'payment_card_cvv', 'billing_address')

class MedicalHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = ('user', 'current_medications', 'family_medical_history', 'past_medications', 'allergies', 'medical_history')

class RolesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Roles
        fields = ('role')

class UserRolesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRoles
        fields = ('user', 'roles', 'role_id', 'time_edited', 'deleted')

class MeasurementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurements
        fields = ('user', 'temperature', 'blood_pressure', 'pulse', 'blood_oxygen', 'weight', 'height')

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('user', 'type', 'date_of_purchase', 'mac', 'user_title', 'firmware_version', 'software_version')


