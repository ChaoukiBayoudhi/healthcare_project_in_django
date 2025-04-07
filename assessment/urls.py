from rest_framework.routers import DefaultRouter
from .views import PatientViewSet,DoctorViewSet,MedicalTestViewSet
from django.urls import path, include
router=DefaultRouter()

#urlp=localhost:8000/health/patients
#add 6 paths
#get all patients: urlp/ (using http method : GET)
#add a patient : urlp/ (using http method : POST)
#get a patient by id : urlp/5 (using http method : GET) (return the patient having the id=5)
#update a patient by id : urlp/5 (using http method : PUT) (complete update)
#patial update of a patient by id : urlp/5 (using http method : PATCH) (patial update)
#delete patient by id : urlp/5 (using http method : DELETE)
router.register('patients',PatientViewSet)
router.register('doctors',DoctorViewSet)
router.register('medical-tests',MedicalTestViewSet)

urlpatterns=[
    path('',include(router.urls)),
]