from django.urls import path
from ReceptionistV.views import *


app_name = 'ReceptionistV'
urlpatterns = [
    path('registration', registration_view),
    path('login', login_view),
    path('home',Receptionist_dash),
    path('logout',Receptionist_Logout),

    path('Doctor/View',Doctor_det),
    path('Doctor/Detail',Doctor_detail),
    path('Doctor/Fees',Doctor_fees),
    path('Doctor/Speciality',Specialization_view),
    path('Doctors',Doctor_det_sp),

    path('Patient/View',Appo_Patient_View),
    path('Patient/Detail',Patient_detail),
    path('Patient/Doc/Detail',Patient_doc_detail),
    path('App/Patient',Patient_det),
    path('Patient/Gender',Patient_gen),
    path('Patient/Pre/Appointment',Patient_Previous_Appointment),
    # path('Patient/Delete',Patient_delete),
    
    path('Notification',Appointment_Noti),
    path('Appointment',Appointment_Request),
    path('Add/Appointment',Add_Appointment),
    
    path('Disease/Patient',Disease_Search),
    path('Disease/View',Disease_view),

    path('Patient/App/Date',Appointment_Date_Search),
    
    
    
 ] 
 