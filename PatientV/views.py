from django.shortcuts import render
import json
import string
import random
import datetime
from django.http  import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import P_Detail,P_Appointment,P_Security
from DoctorV.models import D_Detail
import re


def registration_view(request):
    if request.method == 'POST':
         data = json.loads(request.body)
         First_Name_r         = data['First_Name']
         Last_Name_r          = data['Last_Name']
         Username_r           = data['Username']
         DOB_r                = data['DOB']
         Email_r              = data['Email']
         Password_r           = data['Password']
         C_Password_r         = data['C_Password']
         Mobile_Number_r      = data['Mobile_Number']
         Gender_r             = data['Gender']
         Government_ID_r      = data['Government_ID']
         Gov_ID_Number_r      = data['Gov_ID_Number']
         Height_r             = data['Height']
         Weight_r             = data['Weight']
         Blood_Group_r        = data['Blood_Group']
         Address_r            = data['Address']
         City_r               = data['City']
         State_r              = data['State']
         Country_r            = data['Country']
         Pincode_r            = data['Pincode']
         
         email_condition = "^[a-zA-Z0-9\-\_\.]+@[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}$"
         match = re.search(email_condition,Email_r) 
         
         if (not First_Name_r):
             mes = {
             'message': 'First Name Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not Last_Name_r):
             mes = {
              'message': 'Last Name Required!!'
             }
             return JsonResponse(mes,status=403,safe=False) 
         if (not Username_r):
             mes = {   
              'message': 'Username Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)

         if (P_Detail.objects.filter(Username = Username_r)):
             mes = {    
             'message': 'Username Already Exists!!'
             }
             return JsonResponse(mes,status=403,safe=False)
        
         if (not DOB_r):
             mes = {   
              'message': 'DOB Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)        
         if (not Email_r):
             mes = {    
             'message': 'Email Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)    
         if (not match):
             mes = {    
             'message': 'Invalid Email!!'
             }
             return JsonResponse(mes,status=403,safe=False)   

         if (not Password_r):
             mes = {    
             'message': 'Password Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not C_Password_r):
             mes = {    
             'message': 'Confirm Password Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not Mobile_Number_r):
             mes = {    
             'message': 'Mobile Number Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not Gender_r):
             mes = {      
             'message': 'Gender Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not Government_ID_r):
             mes = {      
             'message': 'Government ID Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not Gov_ID_Number_r):
             mes = {      
             'message': 'Government ID Number Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         
         if (P_Detail.objects.filter(Gov_ID_Number = Gov_ID_Number_r)):
             mes = {    
             'message': 'Government Id Already Exists!!'
             }
             return JsonResponse(mes,status=403,safe=False)   
         if (not Address_r):
             mes = {      
             'message': 'Address Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not City_r):
             mes = {      
             'message': 'City Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not State_r):
             mes = {      
             'message': 'State Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)    
         if (not Country_r):
             mes = {      
             'message': 'Country Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not Pincode_r):
             mes = {      
             'message': 'Pincode Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)                       

         if (Password_r != C_Password_r):
             mes = {    
             'message': 'Password do not Match!!'
             }
             return JsonResponse(mes,status=403,safe=False) 
             
         else:
          Password_h = make_password(Password_r)
          new_user = P_Detail(First_Name=First_Name_r, Last_Name=Last_Name_r, Username=Username_r, DOB=DOB_r, Email=Email_r, Password=Password_h,Mobile_Number=Mobile_Number_r, Gender=Gender_r, Government_ID=Government_ID_r, Gov_ID_Number=Gov_ID_Number_r, Height=Height_r, Weight=Weight_r, Blood_Group=Blood_Group_r, Address=Address_r, City=City_r, State=State_r, Country=Country_r, Pincode=Pincode_r)
          new_user.save()
          mes = {  
          'message': 'User Created Successfully'
           }
          return JsonResponse(mes,status=200,safe=False)




def login_view(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        User_l = data['Username']
        Password_l = data['Password']
        if (P_Detail.objects.filter(Username = User_l).exists()):
                User_list    = P_Detail.objects.filter(Username = User_l)[0]
                Password_c   = User_list.Password
                Password_cr  = check_password(Password_l , Password_c)
                a=list((string.ascii_letters+string.digits+"!@#$%^&*"))
                s=""
                for i in range(20):
                 b=random.choice(a)
                 s+=b
                x=P_Detail.objects.get(Username=User_l) 
                if Password_cr:
                    Secu = P_Security(Patient=x,Username=User_l,Token=s)
                    Secu.save()
                    mes = { 
                    'message'    :'Login Successful!!',
                    'Token'      :s
                    }
                    return JsonResponse(mes,status=200,safe=False)
                    
                else:
                    mes = {
                    'message':'Wrong Password!!'
                    }
                    return JsonResponse(mes,status=403,safe=False)

        else:
             
             mes = {
             'message':'Invalid User!!'
             }
             return JsonResponse(mes,status=403,safe=False)


def Patient_dash(request):
        if request.method == 'POST':
        
             data = json.loads(request.body)     
             Token_d = data['Token']

             if (P_Security.objects.filter(Token = Token_d).exists()):
               Patient_s       =P_Security.objects.filter(Token = Token_d)[0]
               Username_d      = Patient_s.Username
               User_li      = P_Detail.objects.filter(Username = Username_d)
               User_det     = list(User_li.values('id','First_Name','Last_Name','Username','DOB','Email','Mobile_Number','Gender','Government_ID',        'Gov_ID_Number','Height','Weight','Blood_Group','Address','City','State','Country','Pincode'))[0]

              
               mes = {      
                    'User_detail'    :User_det
                    }
               return JsonResponse(mes,status=200,safe=False)
             else:   
               mes = {
                        'message':'Invalid Login attempt!'
                     }
               return JsonResponse(mes,status=403,safe=False)


def Patient_Logout(request):
    if request.method == 'POST':
        data = json.loads(request.body)     
        Token_d = data['Token']               
        Secu = P_Security.objects.get(Token=Token_d)
        Secu.delete()
        mes = {      
        'message'    :"Token Deleted!"
        }
        return JsonResponse(mes,status=200,safe=False)               



def Appointment_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Patient_Age_l      = data['Patient_Age']
        Patient_Disease_l  = data['Patient_Disease']
        Appointment_date_l = data['Appointment_date']
        Appointment_time_l = data['Appointment_time']
        id_l               = data['id']

        Token_d = data['Token']

        if (P_Security.objects.filter(Token = Token_d).exists()):
             Patient_s       =P_Security.objects.filter(Token = Token_d)[0]
             Username_d      = Patient_s.Username
             if (not Patient_Age_l):
                  mes = {
                    'message': 'Patient Age Required!!'
                   }
                  return JsonResponse(mes,status=403,safe=False)
             if (not Patient_Disease_l):
                  mes = {
                    'message': 'Patient Disease Required!!'
                   }
                  return JsonResponse(mes,status=403,safe=False) 
             if (not Appointment_date_l):
                   mes = { 
                    'message': 'Appointment date Required!!'
                  }
                   return JsonResponse(mes,status=403,safe=False)
             if (not Appointment_time_l):
                   mes = { 
                    'message': 'Appointment time Required!!'
                    }
                   return JsonResponse(mes,status=403,safe=False)     
    
             if (P_Detail.objects.filter(Username = Username_d).exists()):
    
                  Patient_l=P_Detail.objects.filter(Username=Username_d)[0]
                  App=D_Detail.objects.get(id=id_l)
                  First=App.First_Name
                  Last=App.Last_Name
                  Appointed_Doctor_l="Dr."+First+" "+Last
                  new_appointment = P_Appointment(Patient=Patient_l,Patient_Age=Patient_Age_l, Patient_Disease=Patient_Disease_l, Appointment_date=Appointment_date_l,Appointment_time=Appointment_time_l,Appointed_Doctor=Appointed_Doctor_l)
                  new_appointment.save()
    
                  mes = { 
                       'message'   :'Appointment Request Generated!!'
                       }
                  return JsonResponse(mes,status=200,safe=False)

def Payment_view(request):
    if request.method == 'POST':
         data = json.loads(request.body)
         id_d = data['id']
         Patient_s        =P_Appointment.objects.filter(id = id_d)[0]
         id_p             = Patient_s.id
         x = datetime.datetime.now()
         obj = P_Appointment.objects.get(id=id_p)
         obj.Payment_Status="Waiting For Approval"
         obj.Payment_Time=x
         obj.save(update_fields=['Payment_Status','Payment_Time'])
         mes = { 
                'message' :'Payment done Successfully!'
               }
         return JsonResponse(mes,status=200,safe=False)


             


def Doctor_det(request):
    if request.method == 'POST':
        if(D_Detail.objects.exists()):
           doctor_det = D_Detail.objects.all()
           Doctor_data = list(doctor_det.values('id','First_Name','Last_Name','Speciality'))
           mes = {      
           'Doctor_detail'    :Doctor_data
           }
           return JsonResponse(mes,status=200,safe=False)
        else:
            mes = {      
           'Doctor_detail'    :"No Doctor Registered!"
           }
            return JsonResponse(mes,status=200,safe=False)

def Doctor_fees(request):
     data = json.loads(request.body)
     id_l   = data['id']
     App=D_Detail.objects.get(id=id_l)
     Fees=App.Appointment_fees
     mes = { 
           'Doctor_fees' :Fees
           }
     return JsonResponse(mes,status=200,safe=False)


def Appointment_History(request):
    data = json.loads(request.body)
    Token_d = data['Token']

    if (P_Security.objects.filter(Token = Token_d).exists()):
          Patient_s       =P_Security.objects.filter(Token = Token_d)[0]
          Patient_s       =P_Security.objects.filter(Token = Token_d)[0]
          id_d            = Patient_s.Patient
          App_His=P_Appointment.objects.filter(Patient=id_d)
      
          Appointment_det     = list(App_His.values('id','Patient_Age','Patient_Disease','Appointment_date','Appointment_time','Appointment_Status',      'Appointed_Doctor','Prescription','Payment_Status','Payment_Time','Appointment_reg_at'))
      
          mes = {      
                'Appointment_Hist'    : Appointment_det
                }
          return JsonResponse(mes,status=200,safe=False)

  
        
         