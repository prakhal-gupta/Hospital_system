from django.urls import path
from DoctorV.views import registration_view,login_view,Appointment_St_Up,Add_Appointment,Doctor_dash,Patient_detail,Doctor_Logout,Appointments,Appointment_Noti,Patient_Prescription,Patient_Pres_data


app_name = 'DoctorV'
urlpatterns = [
 	path('registration',registration_view),
    path('login',login_view),
    path('Appointment/Status',Appointment_St_Up),
    path('Add/Appointment',Add_Appointment),
    path('home',Doctor_dash),
    path('Patients',Patient_detail),
    path('logout',Doctor_Logout),
    path('Appointments',Appointments),
    path('Appointment/Notification',Appointment_Noti),
    path('Patient/Prescription',Patient_Prescription),
    path('Patient/Detail',Patient_Pres_data),

 ] 
 
