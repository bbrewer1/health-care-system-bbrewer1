from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    birth_date = models.DateField()
    address = models.CharField(max_length=60)
    pcp = models.CharField(max_length=60)
    sex = models.CharField(max_length=2)
    emergency_contacts = models.CharField(max_length=60)
    def __str__(self):
        return self.id

class BillingInfo(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    insurance_company = models.CharField(max_length=60)
    member_id = models.CharField(max_length=15)
    member_name = models.CharField(max_length = 30)
    saved_credit_cards = models.IntegerField()
    billing_address = models.CharField(max_length = 60)
    def __str__(self):
        return self.id

class MedicalHistory(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    current_medication = models.CharField(max_length = 200)
    family_medical_history = models.CharField(max_length=200)
    past_medications = models.CharField(max_length=200)
    allergies = models.CharField(max_length=200)
    medical_history = models.CharField(max_length=200)
    def __str__(self):
        return self.id

class Roles(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    role = models.CharField(max_length = 20)
    def __str__(self):
        return self.id

class UserRoles(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    rid = models.IntegerField
    delete = models.CharField(max_length=10)
    time = models.TimeField()
    def __str__(self):
        return self.id

class Measurements(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    temperature = models.FloatField()
    blood_pressure = models.CharField(max_length = 10)
    pulse = models.IntegerField()
    blood_oxygen = models.FloatField()
    weight = models.FloatField()
    height = models.CharField(max_length=10)
    def __str__(self):
        return self.id

class Device(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    type = models.CharField(max_length = 20)
    date_of_purcahse = models.DateField()
    mac = models.CharField(max_length = 20)
    user_title = models.CharField(max_length = 20)
    firmware_version = models.CharField(max_length = 10)
    software_version = models.CharField(max_length = 10)
    def __str__(self):
        return self.id
