from django.urls import path
from PatientV.views import *

app_name = 'PatientV'
urlpatterns = [
 	 path('registration', registration_view),
    path('login', login_view),
    path('home', Patient_dash),
    path('logout', Patient_Logout),

    path('Appointment', Appointment_view),
    path('Appointment/Payment', Payment_view),
    path('Appointment/Doctors', Doctor_det_sp),
    path('Doctors', Doctor_det),
    path('Appointment/Doctor/Fees', Doctor_fees),
    path('Appointment/History', Appointment_History),
    path('App/Update',Time_Change),
   
    path('Prescription', Prescription_view ),
    path('Prescription/det', Prescription_det ),
    
    path('Payment/History',Payment_History),
    path('Payment/Receipt',Payment_Receipt),
    
    path('Disease/reg', Disease_reg),
    path('Disease', Disease_view ),

    path('Doc/Specialization',Specialization_view),

   #  path('SMS',send_sms),
    path('Pass/Change',Password_Change),
   #  path('OTP/Verification',OTP_Verification),

 ] 
 
