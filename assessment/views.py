from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import HealthRecord, Patient,Doctor,MedicalTest
from .serializers import (PatientSerializer,
                    DoctorSerializer,
                    MedicalTestSerializer,
                    HealthRecordSerializer)
#define the CRUD (Create, Read/Retreive, Update and Delete) on Patient model
class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
    #http_method_names=['GET','POST','DELETE']
class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    @action(methods=['get'], detail=False, 
            url_path='by_speciality/(?P<speciality>[^/.]+)')
    def get_doctors_by_speciality(self,request,speciality):
        result=Doctor.objects.filter(specialty__iexact=speciality)
        if not result.exists():
            return Response(data='There is no doctor hasing the speciality '+speciality,
                            status=status.HTTP_204_NO_CONTENT)
        serialized_result=DoctorSerializer(result,many=True)
        #or
        #serialized_result=self.get_serializer(result,many=True)
        return Response(serialized_result.data,status=status.HTTP_200_OK)
    

class MedicalTestViewSet(viewsets.ModelViewSet):
    queryset=MedicalTest.objects.all()
    serializer_class=MedicalTestSerializer

class HealthRecordViewSet(viewsets.ModelViewSet):
    queryset=HealthRecord.objects.all()
    serializer_class=HealthRecordSerializer

    @action(methods=['GET'],detail=False)
    def get_patients_by_doctor(self,request,doctor_id):
            try:
                doctor=Doctor.objects.get(id=doctor_id)
            except Doctor.DoesNotExist:
                return Response(data='There is no doctor hasing the id '+doctor_id,
                                status=status.HTTP_204_NO_CONTENT)
