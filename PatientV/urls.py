from django.urls import path
from PatientV.views import registration_view,login_view,Patient_dash,Appointment_view,Patient_Logout,Payment_view,Doctor_det,Doctor_fees,Appointment_History

app_name = 'PatientV'
urlpatterns = [
 	 path('registration', registration_view, name="register"),
    path('login', login_view, name="loginp"),
    path('home', Patient_dash, name="homep"),
    path('logout', Patient_Logout, name="logoutp"),
    path('Appointment', Appointment_view, name="Appointmentp"),
    path('Appointment/Payment', Payment_view, name="Appointmentpay"),
    path('Appointment/Doctors', Doctor_det, name="Appointmentdoctorp"),
    path('Appointment/Doctor/Fees', Doctor_fees, name="Appointmentdoctorfeesp"),
    path('Appointment/History', Appointment_History, name="Appointmenthistoryp"),

 ] 
 
