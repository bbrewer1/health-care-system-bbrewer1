from django.db import models
import uuid
import datetime

# Create your models here.
class User(models.Model):
    id = models.UUIDField('UID', primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=60, default = "Jane")
    last_name = models.CharField(max_length=60, default = "Doe")
    birth_date = models.DateField(default = "01/01/2000")
    address = models.CharField(max_length=60, default = "3 Dover ct")
    pcp = models.CharField(max_length=60, default = "Cynthia Mann")
    sexes = (('M', 'Male'), ('F', 'Female'))
    sex = models.CharField(max_length=1, choices=sexes)
    emergency_contacts = models.CharField(max_length=60, default = "John Smith")
    def __str__(self):
        return self.first_name + " " + self.last_name

class BillingInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="temp")
    insurance_company = models.CharField(max_length=60, default = "Athem Blue Cross")
    member_id = models.CharField(max_length=15, default="A1B2")
    member_name = models.CharField(max_length = 80, default = "Jane Doe")
    payment_card_number = models.CharField(max_length=16, default='NA')
    payment_card_expiration = models.DateField('Expiration Date', default=datetime.date.today)
    payment_card_cvv = models.CharField('CVV', max_length=3, default = '000')
    billing_address = models.CharField(max_length = 60, default = "3 Dover ct")
    def __str__(self):
        return self.member_name + " " + self.billing_address

class MedicalHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="temp")
    current_medication = models.CharField(max_length = 200, default = "NA")
    family_medical_history = models.CharField(max_length=200, default="NA")
    past_medications = models.CharField(max_length=200, default="NA")
    allergies = models.CharField(max_length=200, default="NA")
    medical_history = models.CharField(max_length=200, default="NA")

class Roles(models.Model):
    role = models.CharField(max_length = 20, default="User")
    def __str__(self):
        return self.role

class UserRoles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="temp")
    roles = ((1, 'Patient'), (2, 'Nurse'), (3, 'Doctor'), (4, 'Admin'), (5, 'Gaurdian'))
    role_id = models.IntegerField(choices = roles, default=1)
    time_edited = models.TimeField(auto_now=True)
    deleted = models.BooleanField(default=0)

class Measurements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="temp")
    temperature = models.FloatField(default = 98.6)
    blood_pressure = models.CharField(max_length = 10, default = "120/80")
    pulse = models.IntegerField(default = 60)
    blood_oxygen = models.FloatField(default=95.0)
    weight = models.FloatField(default=130.0)
    height = models.CharField(max_length=10, default="5'4")
    def __str__(self):
        return self.height + " " + str(self.weight)

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="temp")
    type = models.CharField(max_length = 20, default="MRI")
    date_of_purcahse = models.DateField(default="1/1/2000")
    mac = models.CharField(max_length = 20, default="AB:12:CD:34:EF:56")
    user_title = models.CharField(max_length = 20, default="Doctor")
    firmware_version = models.CharField(max_length = 10, default="1.0.0")
    software_version = models.CharField(max_length = 10, default="1.0.0")
    def __str__(self):
        return self.type + " " + self.mac
