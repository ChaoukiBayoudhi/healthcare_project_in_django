from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

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
    @action(methods=['GET'])
    def get_doctors_by_speciality(self,request,speciality):
        result=Doctor.objects.filter(speciality__iexact=speciality)
        if not result.exists():
            return Response(data='There is no doctor hasing the speciality'+speciality,
                            status=status.HTTP_204_NO_CONTENT)
        serialized_result=DoctorSerializer(result,many=True)
        #or
        #serialized_result=self.get_serializer(result,many=True)
        return Response(serialized_result.data,status=status.HTTP_200_OK)


class MedicalTestViewSet(viewsets.ModelViewSet):
    queryset=MedicalTest.objects.all()
    serializer_class=MedicalTestSerializer