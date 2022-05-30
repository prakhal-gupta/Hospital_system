from django.shortcuts import render,get_object_or_404
import json
import string
import random
import datetime
from django.http  import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import R_Detail,R_Security
from PatientV.models import P_Appointment,P_Detail,P_Disease
from DoctorV.models import D_Detail,D_Specialization
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

         if (R_Detail.objects.filter(Username = Username_r)):
             mes = {   
             'message': 'Username Already Exists!!'
             }
             return JsonResponse(mes,safe=False)
        
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
         
         match = re.search(email_condition,Email_r)
         
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
          new_user = R_Detail(First_Name=First_Name_r, Last_Name=Last_Name_r, Username=Username_r, DOB=DOB_r, Email=Email_r, Password=Password_h,Mobile_Number=Mobile_Number_r, Gender=Gender_r, Government_ID=Government_ID_r, Gov_ID_Number=Gov_ID_Number_r, Height=Height_r, Weight=Weight_r, Blood_Group=Blood_Group_r, Address=Address_r, City=City_r, State=State_r, Country=Country_r, Pincode=Pincode_r)
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
        if (R_Detail.objects.filter(Username = User_l).exists()):
                User_list = R_Detail.objects.filter(Username = User_l)[0]
                Password_c = User_list.Password
                Password_cr = check_password(Password_l , Password_c)
                a=list((string.ascii_letters+string.digits+"!@#$%^&*"))
                s=""
                for i in range(20):
                 b=random.choice(a)
                 s+=b
                x=R_Detail.objects.get(Username=User_l)
                
                
                if Password_cr:
                    Secu = R_Security(Receptionist=x,Username=User_l,Token=s)
                    Secu.save()
                    mes = {                    
                    'message':'Login Successful!!',
                    'Token': s
                    }
                    d={''}
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




def Receptionist_dash(request):
        if request.method == 'POST':
        
             data = json.loads(request.body)     
             Token_d = data['Token']

             if (R_Security.objects.filter(Token = Token_d).exists()):
               Receptionist_s  =R_Security.objects.filter(Token = Token_d)[0]
               Username_d      = Receptionist_s.Username
               Receptionist_li         = R_Detail.objects.filter(Username = Username_d)
               Receptionist_det        = list(Receptionist_li.values('id','First_Name','Last_Name','Username','DOB','Email','Mobile_Number','Gender','Government_ID','Gov_ID_Number','Height','Weight','Blood_Group','Address','City','State','Country','Pincode'))[0]
              
               mes = {      
                    'Receptionist_detail'  :Receptionist_det,
                    }
               return JsonResponse(mes,status=200,safe=False)
             else:   
               mes = {
                        'message':'Invalid Login attempt!'
                     }
               return JsonResponse(mes,status=403,safe=False)




def Receptionist_Logout(request):
    if request.method == 'POST':
        data = json.loads(request.body)     
        Token_d = data['Token']               
        Secu = R_Security.objects.get(Token=Token_d)
        Secu.delete()
        mes = {      
        'message'    :"Token Deleted!"
        }
        return JsonResponse(mes,status=200,safe=False)



def Doctor_detail(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_d = data['id']
        
        Doctor_d = D_Detail.objects.filter(id = id_d)
        Doctor_det = list(Doctor_d.values('id','First_Name','Last_Name','Username','DOB','Email','Mobile_Number','Gender','Blood_Group','Qualification','Speciality','Experience','Previously_Working_at','Address','City','State','Country','Pincode'))[0]

        mes={
                'Doctor_detail'   :Doctor_det
                }
        return JsonResponse(mes,status=200,safe=False)


def Doctor_det(request):
    if request.method == 'POST':
       data = json.loads(request.body)
       Token_d       = data['Token']

       if (R_Security.objects.filter(Token = Token_d).exists()): 
         if(D_Detail.objects.exists()):
           doctor_det = D_Detail.objects.all()
           Doctor_data = list(doctor_det.values('id','First_Name','Last_Name','Username','Speciality','Mobile_Number','Email'))
           mes = {      
           'Doctor_detail'    :Doctor_data
           }
           return JsonResponse(mes,status=200,safe=False)
         else:
            mes = {      
           'message'    :"No Doctor Registered!"
           }
            return JsonResponse(mes,status=403,safe=False)


def Doctor_fees(request):
     data = json.loads(request.body)
     id_l   = data['id']
     App=D_Detail.objects.get(id=id_l)
     Fees=App.Appointment_fees
     mes = { 
           'Doctor_fees' :Fees
           }
     return JsonResponse(mes,status=200,safe=False) 


def Specialization_view(request):
    if request.method == 'POST':
        Speci= D_Specialization.objects.all()
        Spec= []
        for i in Speci:
             Spec.append({'Spec':i.Specialization})

        mes = {
                  'Spe' :Spec
              }
        return JsonResponse(mes,status=200,safe=False)            





def Patient_detail(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_d = data['id']
    
        Patient_d = P_Detail.objects.filter(id = id_d)
     
        Patient_det = list(Patient_d.values('id','First_Name','Last_Name','Username','DOB','Email','Mobile_Number','Gender','Blood_Group','Address','City','State','Country','Pincode'))[0]

        mes={
                'Patient_detail'   :Patient_det
                }
        return JsonResponse(mes,status=200,safe=False)       



def Patient_doc_detail(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_d = data['id']

        User_list = D_Detail.objects.filter(id = id_d)[0]
        First_N    = User_list.First_Name
        Last_N     = User_list.Last_Name
        Name       = "Dr." + First_N + " " + Last_N

        if (P_Appointment.objects.filter(Appointed_Doctor = Name).exists()):
             Patient_l       = P_Appointment.objects.filter(Appointed_Doctor = Name)
             Patient_det= []
             for i in Patient_l:               

                Patient_det.append({"id":i.Patient.id,"F_Name":i.Patient.First_Name,"L_Name":i.Patient.Last_Name,"Usern":i.Patient.Username,"dob":i.Patient.DOB,"email":i.Patient.Email,"M_No":i.Patient.Mobile_Number,"Gend":i.Patient.Gender,"blood_group":i.Patient.Blood_Group})

             mes = {
                    'Patient_detail' :Patient_det
                   }
             return JsonResponse(mes,status=200,safe=False)


def Patient_det(request):
    if request.method == 'POST':
       data = json.loads(request.body)
       Token_d       = data['Token']

       if (R_Security.objects.filter(Token = Token_d).exists()): 
         if(P_Detail.objects.exists()):
           Patient_det = P_Detail.objects.all()
           Patient_data = list(Patient_det.values('id','First_Name','Last_Name'))
           mes = {      
           'Patient_detail'    :Patient_data
           }
           return JsonResponse(mes,status=200,safe=False)
         else:
            mes = {      
           'message'    :"No Patient Registered!"
           }
            return JsonResponse(mes,status=403,safe=False) 


def Patient_gen(request):
    if request.method == 'POST':
       data = json.loads(request.body)
       id_l   = data['id']
       Patient_det = P_Detail.objects.get(id=id_l)
       Gen = Patient_det.Gender
       mes = {      
           'Patient_gender'    :Gen
           }
       return JsonResponse(mes,status=200,safe=False)



def Appo_Patient_View(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Token_d = data['Token']
        
        if (R_Security.objects.filter(Token = Token_d).exists()):
            Patient_det = list(P_Detail.objects.values('id','First_Name','Last_Name','Username','DOB','Email','Mobile_Number','Gender'))

            mes={
                'Patient_detail'   :Patient_det
                }
            return JsonResponse(mes,status=200,safe=False)


def Patient_Previous_Appointment(request):
     data = json.loads(request.body)
     id_d = data['id']      
     if(P_Appointment.objects.filter(Patient=id_d).exists()):
         Patient_a =P_Appointment.objects.filter(Patient=id_d)
         Patient_det = list(Patient_a.values('id','Patient_Age','Patient_Disease','Appointment_date','Appointment_time','Appointment_Status','Appointed_Doctor','Prescription','Diagnosis','Payment_Status','Payment_Time','Appointment_reg_at'))

         mes={
                'Patient_Appointment'   :Patient_det
                }
         return JsonResponse(mes,status=200,safe=False)


def Patient_delete(request):
    
    if request.method == "POST":
        data = json.loads(request.body)
        id_p          = data['id']

        if(P_Detail.objects.filter(id = id_p).exists()):  
            obj = get_object_or_404(P_Detail, id=id_p)
            obj.delete()                   
            mes = { 
               'message' :'Patient Deleted Successfully!',
                }
            return JsonResponse(mes,status=200,safe=False)         





def Appointment_Noti(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Token_d = data['Token']
        if (R_Security.objects.filter(Token = Token_d).exists()):

              Patient_d       = P_Appointment.objects.filter(Appointment_Status="Pending",Payment_Status="Waiting For Approval")
              if(Patient_d):

                 Patient_det= []
                 for i in Patient_d:               
                   
                   Patient_det.append({"ID":i.id,"F_Name":i.Patient.First_Name,"L_Name":i.Patient.Last_Name,"App_date":i.Appointment_date,"App_time":i.Appointment_time,"Pat_disease":i.Patient_Disease,"App_Doc":i.Appointed_Doctor,"App_Stat":i.Appointment_Status})

                 mes = {
                          'Appointment_detail' :Patient_det
                       }
                 return JsonResponse(mes,status=200,safe=False)    
              else:
                 mes = {
                          'message' :"No Approval Pending!"
                       }
                 return JsonResponse(mes,status=403,safe=False)



def Appointment_Request(request):
    if request.method == 'POST':
        
         data = json.loads(request.body)
         id_d   = data['id']
         App_p  = data['Appointment_St']
         App = P_Appointment.objects.filter(id = id_d)[0]
         App_s = App.Appointment_Status
         if(App_s=="Pending"):

            if(App_p=="Accept"):
               obj = P_Appointment.objects.get(Patient=id_d)
               obj.Appointment_Status="Waiting For Doctor's Approval"
               obj.Payment_Status="Successful"
               obj.save(update_fields=['Appointment_Status','Payment_Status'])
               mes = { 
                       'message' :'Appointment Approved!'
                         }
               return JsonResponse(mes,status=200,safe=False)
            if(App_p=="Reject"):
               App_rej = data['Reason']
               if (not App_rej):
                   mes = {
                         'message': 'Rejection Reason Required!!'
                        }
                   return JsonResponse(mes,status=403,safe=False)
               obj = P_Appointment.objects.get(Patient=id_d)
               obj.Appointment_Status="Rejected"
               obj.Payment_Status="Payment Returned"
               obj.App_Rej_Reason=App_rej
               obj.save(update_fields=['Appointment_Status','App_Rej_Reason','Payment_Status'])
               mes = { 
                      'message' :'Appointment Rejected!'
                        }
               return JsonResponse(mes,status=200,safe=False)



def Add_Appointment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Patient_Age_l      = data['Patient_Age']
        Patient_Disease_l  = data['Patient_Disease']
        Appointment_date_l = data['Appointment_date']
        Appointment_time_l = data['Appointment_time']
        id_d               = data['Id_d']
        id_p               = data['Id_p']
        Token_d            = data['Token']

        if (R_Security.objects.filter(Token = Token_d).exists()):
            
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
    
            
             Patient_l=P_Detail.objects.filter(id = id_p)[0]
             App=D_Detail.objects.get(id=id_d)
             First=App.First_Name
             Last=App.Last_Name
             Appointed_Doctor_l="Dr."+First+" "+Last
             x = datetime.datetime.now()
             new_appointment = P_Appointment(Patient=Patient_l,Patient_Age=Patient_Age_l, Patient_Disease=Patient_Disease_l, Appointment_date=Appointment_date_l,Appointment_time=Appointment_time_l,Appointed_Doctor=Appointed_Doctor_l,Appointment_Status="Waiting For Doctor's Approval",Payment_Status="Successful",Payment_Time=x)
             new_appointment.save() 
             mes = { 
                  'message'   :'Appointment Fixed!!'
                  }
             return JsonResponse(mes,status=200,safe=False)





def Disease_Search(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Token_d = data['Token']
        Dis     = data['Disease']
        if (R_Security.objects.filter(Token = Token_d).exists()):

              Patient_d       = P_Appointment.objects.filter(Patient_Disease=Dis)
              if(Patient_d):

                 Patient_det= []
                 for i in Patient_d:               
                   
                   Patient_det.append({"ID":i.id,"F_Name":i.Patient.First_Name,"L_Name":i.Patient.Last_Name,"App_date":i.Appointment_date,"App_time":i.Appointment_time,"Pat_disease":i.Patient_Disease,"App_Doc":i.Appointed_Doctor,"App_Stat":i.Appointment_Status})

                 mes = {
                          'Patient_detail' :Patient_det
                       }
                 return JsonResponse(mes,status=200,safe=False)    
              else:
                 mes = {
                          'message' :"No Patient Found!"
                       }
                 return JsonResponse(mes,status=403,safe=False) 


def Disease_view(request):
    if request.method == 'POST':
        Dise = P_Disease.objects.all()
        Disease= []
        for i in Dise:
             Disease.append({'Disea':i.Disease})

        mes = {
                  'Des' :Disease
              }
        return JsonResponse(mes,status=200,safe=False) 




  






                          







