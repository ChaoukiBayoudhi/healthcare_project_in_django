from django.contrib import admin

# Register your models here.
from .models import Patient, Doctor, MedicalTest, HealthRecord,Prediction
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(MedicalTest)
admin.site.register(HealthRecord)
admin.site.register(Prediction)
