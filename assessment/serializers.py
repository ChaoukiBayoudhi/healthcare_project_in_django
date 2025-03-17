from rest_framework import serializers
from .models import Patient
class PatientSeializer(serializers.ModelSeializer):
    class Meta:
        model=Patient
        #fields=['full_name', 'date_of_birth','gender']
        fields='__all__'
