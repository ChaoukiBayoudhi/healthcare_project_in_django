from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from django.core.validators import ValidationError


#Model Patient  (OneToOne | Patient → User)
#class Patient(User):
class Patient(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(validators=[MinValueValidator(date(1950,1,1))])
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    medical_history = models.TextField(blank=True, null=True)

    class Meta:
        db_table='patient'
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name
    
class DoctorSpeciality(models.TextChoices):
    CARDIOLOGIST = 'Cardiologist'
    DERMATOLOGIST = 'Dermatologist'
    GASTROENTEROLOGIST = 'Gastroenterologist'
    GENERAL_PRACTITIONER = 'General Practitioner'
    NEUROLOGIST = 'Neurologist'
    ONCOLOGIST = 'Oncologist'
    OPHTHALMOLOGIST = 'Ophthalmologist'
    ORTHOPEDIC_SURGEON = 'Orthopedic Surgeon'
    OTOLARYNGOLOGIST = 'Otolaryngologist'
    PEDIATRICIAN = 'Pediatrician'
    PSYCHIATRIST = 'Psychiatrist'
    UROLOGIST = 'Urologist'
#Model Doctor (OneToOne | Doctor → User)
#class Doctor(User):
class Doctor(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=20, choices=DoctorSpeciality.choices, default=DoctorSpeciality.GENERAL_PRACTITIONER)
    hospital = models.CharField(max_length=255, blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(validators=[MinValueValidator(2),MaxValueValidator(10)])

    class Meta:
        db_table='doctor'
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return f"Dr. {self.user.get_full_name()}"
def TestNameValidator(value):
        if not value.upper().startswith('TEST'):
            raise ValidationError("Test name must start with 'Test'")
        if 'HIV' in value.upper():
            raise ValidationError("This test is not allowed.")
       
#MedicalTest Model (ManyToMany | HealthRecord → MedicalTest )
class MedicalTest(models.Model):
     
    name = models.CharField(max_length=255,
                            validators=[TestNameValidator])
    result = models.CharField(max_length=255)
    date = models.DateField(default=date.today)
    health_records = models.ManyToManyField("HealthRecord", blank=True)
    #redefinition of clean method
    #if the test date is older than 7 days, raise a validation error
    def clean(self):
        if (date.today() - self.date).days > 7:
            raise ValidationError("Test date cannot be older than 7 days. You have to redo the test.")
    class Meta:
        db_table='medical_test'
        verbose_name = "Medical Test"
        verbose_name_plural = "Medical Tests"

    def __str__(self):
        return f"{self.name} - {self.result} ({self.date})"

#HealthRecord Model (OneToMany |Doctor → HealthRecord)
# (ManyToMany | HealthRecord → MedicalTest )
class HealthRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    blood_pressure = models.CharField(max_length=20)
    cholesterol = models.CharField(max_length=20)
    bmi = models.FloatField()
    diabetes_history = models.BooleanField(default=False)
    medical_tests = models.ManyToManyField(MedicalTest, blank=True)

    class Meta:
        db_table='health_record'
        verbose_name = "Health Record"
        verbose_name_plural = "Health Records"

    def __str__(self):
        return f"Health Record for {self.patient.full_name}"
    


class Prediction(models.Model):
    condition_type = models.CharField(max_length=30, choices=[("diabetes", "diabetes"), ("hypertension", "hypertension")])
    risk_score = models.FloatField()
    prediction_date = models.DateField(auto_now=True)
    health_record = models.ForeignKey(HealthRecord, on_delete=models.CASCADE, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table='predication'
        verbose_name = "Prediction"
        verbose_name_plural = "Predictions"

    def __str__(self):
        return f"Prediction for {self.health_record.patient.full_name} - {self.condition_type}"
