from rest_framework import viewsets

from .models import Patient,Doctor,MedicalTest
from .serializers import PatientSerializer,DoctorSerializer,MedicalTestSerializer
#define the CRUD (Create, Read/Retreive, Update and Delete) on Patient model
class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
    #http_method_names=['GET','POST','DELETE']
class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer

class MedicalTestViewSet(viewsets.ModelViewSet):
    queryset=MedicalTest.objects.all()
    serializer_class=MedicalTestSerializer