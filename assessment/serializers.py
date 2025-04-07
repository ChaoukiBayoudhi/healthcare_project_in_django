from rest_framework import serializers
from .models import Patient, Doctor,MedicalTest
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