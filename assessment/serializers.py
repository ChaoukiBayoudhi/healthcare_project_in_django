from rest_framework import serializers
from .models import Patient, Doctor,MedicalTest,HealthRecord
class PatientSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model=Patient
        #fields=['full_name', 'date_of_birth','gender']
        fields='__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'

class MedicalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicalTest
        fields='__all__'


class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=HealthRecord
        fields='__all__'