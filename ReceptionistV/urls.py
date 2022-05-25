from django.urls import path
from ReceptionistV.views import registration_view,login_view,Appointment_View,Payment_View,Receptionist_dash,Receptionist_Logout,Patient_delete,Doctor_detail,Patient_detail,App_Patient_View,Add_Appointment,App_Doctor_det,Doctor_fees


app_name = 'ReceptionistV'
urlpatterns = [
    path('registration', registration_view),
    path('login', login_view),
    path('home',Receptionist_dash),
    path('logout',Receptionist_Logout),
    path('Doctor/Detail',Doctor_detail),
    path('Patient/Detail',Patient_detail),
    path('Patient/View',App_Patient_View),
    path('Add/Appointment',Add_Appointment),
    path('Doctor/View',App_Doctor_det),
    path('Doctor/Fees',Doctor_fees),
    path('Appointment',Appointment_View),
    path('Patient/Payment',Payment_View),
    path('Patient/Delete',Patient_delete),
 ] 
 