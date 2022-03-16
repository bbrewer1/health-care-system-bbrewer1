from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    first_name = models.CharField(max_length=60, default = "Jane")
    last_name = models.CharField(max_length=60, default = "Doe")
    birth_date = models.DateField(default = "01/01/2000")
    address = models.CharField(max_length=60, default = "3 Dover ct")
    pcp = models.CharField(max_length=60, default = "Cynthia Mann")
    sex = models.CharField(max_length=2, default = "F")
    emergency_contacts = models.CharField(max_length=60, default = "John Smith")
    def __str__(self):
        return self.first_name + " " + self.last_name

class BillingInfo(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    insurance_company = models.CharField(max_length=60, default = "Athem Blue Cross")
    member_id = models.CharField(max_length=15, default="A1B2")
    member_name = models.CharField(max_length = 30, default = "Jane Doe")
    saved_credit_cards = models.IntegerField(default = "0000111122223333")
    billing_address = models.CharField(max_length = 60, default = "3 Dover ct")
    def __str__(self):
        return self.member_id + " " + self.billing_address

class MedicalHistory(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    current_medication = models.CharField(max_length = 200, default = "NA")
    family_medical_history = models.CharField(max_length=200, default="NA")
    past_medications = models.CharField(max_length=200, default="NA")
    allergies = models.CharField(max_length=200, default="NA")
    medical_history = models.CharField(max_length=200, default="NA")
    def __str__(self):
        return self.medical_history

class Roles(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    role = models.CharField(max_length = 20, default="User")
    def __str__(self):
        return self.role

class UserRoles(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    rid = models.IntegerField
    delete = models.CharField(max_length=10)
    time = models.TimeField()
    def __str__(self):
        return self.rid

class Measurements(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    temperature = models.FloatField(default = 98.6)
    blood_pressure = models.CharField(max_length = 10, default = "120/80")
    pulse = models.IntegerField(default = 60)
    blood_oxygen = models.FloatField(default=95.0)
    weight = models.FloatField(default=130.0)
    height = models.CharField(max_length=10, default="5'4")
    def __str__(self):
        return self.height + " " + str(self.weight)

class Device(models.Model):
    uid = models.CharField(max_length=20, default="user0")
    type = models.CharField(max_length = 20, default="MRI")
    date_of_purcahse = models.DateField(default="1/1/2000")
    mac = models.CharField(max_length = 20, default="AB:12:CD:34:EF:56")
    user_title = models.CharField(max_length = 20, default="Doctor")
    firmware_version = models.CharField(max_length = 10, default="1.0.0")
    software_version = models.CharField(max_length = 10, default="1.0.0")
    def __str__(self):
        return self.type + " " + self.mac
