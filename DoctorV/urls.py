from django.urls import path
from DoctorV.views import *


app_name = 'DoctorV'
urlpatterns = [
 	 path('registration',registration_view),
    path('login',login_view),
    path('home',Doctor_dash),
    path('logout',Doctor_Logout),
    
    path('Appointment/Notification',Appointment_Noti),
    path('Appointment/Status',Appointment_St_Up),
    path('Appointments',Appointments),
    
    path('Patients',Patient_detail),
    path('Patient/Prescription',Patient_Prescription),
    path('Patient/Detail',Patient_Pres_data),
    
    path('Appointment/patient',Add_Appointment_d),
    path('Appointment/patient/gender',Patient_Gender),
    path('Book/Appointment',Add_Appointment),

    path('Previous/Appointment',Previous_Appointment),
    path('Previous/Patient/Prescription',Prescription_view),

    path('Specialization/reg',Specialization_reg),
    path('Specialization',Specialization_view),

    path('Pass/Change',Password_Change),    

] 
 
