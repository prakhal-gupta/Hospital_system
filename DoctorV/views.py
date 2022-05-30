from django.shortcuts import render
import json
import string
import random
import datetime
from django.http  import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import D_Detail,D_Security,D_Specialization
from PatientV.models import P_Appointment,P_Detail
import re

def registration_view(request):
    if request.method == 'POST':
         data = json.loads(request.body)
         First_Name_r              = data['First_Name']
         Last_Name_r               = data['Last_Name']
         Username_r                = data['Username']
         DOB_r                     = data['DOB']
         Email_r                   = data['Email']
         Password_r                = data['Password']
         C_Password_r              = data['C_Password']
         Mobile_Number_r           = data['Mobile_Number']
         Gender_r                  = data['Gender']
         Government_ID_r           = data['Government_ID']
         Gov_ID_Number_r           = data['Gov_ID_Number']
         Height_r                  = data['Height']
         Weight_r                  = data['Weight']
         Blood_Group_r             = data['Blood_Group']
         Qualification_r           = data['Qualification']
         Speciality_r              = data['Speciality']
         Experience_r              = data['Experience']
         Previously_Working_at_r   = data['Previously_Working_at']
         Address_r                 = data['Address']
         City_r                    = data['City']
         State_r                   = data['State']
         Country_r                 = data['Country']
         Pincode_r                 = data['Pincode']
        #  Profile_pic_r             = data['Profile_pic']
         
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

         if (D_Detail.objects.filter(Username = Username_r)):
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
         if (not Qualification_r):
             mes = {     
             'message': 'Qualification Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)        
         if (not Speciality_r):
             mes = {     
             'message': 'Speciality Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (Experience_r and not Previously_Working_at_r):
              mes = {     
             'message': 'Previously Working Place Required!!'
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
          new_user = D_Detail(First_Name=First_Name_r, Last_Name=Last_Name_r, Username=Username_r, DOB=DOB_r, Email=Email_r, Password=Password_h,Mobile_Number=Mobile_Number_r, Gender=Gender_r, Government_ID=Government_ID_r, Gov_ID_Number=Gov_ID_Number_r, Height=Height_r, Weight=Weight_r,Blood_Group=Blood_Group_r, Qualification=Qualification_r, Speciality=Speciality_r,Experience=Experience_r, Previously_Working_at=Previously_Working_at_r, Address=Address_r, City=City_r, State=State_r, Country=Country_r, Pincode=Pincode_r)
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
        if (D_Detail.objects.filter(Username = User_l).exists()):
                User_list = D_Detail.objects.filter(Username = User_l)[0]
                Password_c = User_list.Password
                First_N    = User_list.First_Name
                Last_N     = User_list.Last_Name
                Name       = "Dr." + First_N + " " + Last_N
                Password_cr = check_password(Password_l , Password_c)
                a=list((string.ascii_letters+string.digits+"!@#$%^&*"))
                s=""
                for i in range(20):
                 b=random.choice(a)
                 s+=b
                x=D_Detail.objects.get(Username=User_l)
                
                if Password_cr:
                        Secu = D_Security(Doctor=x,Username=User_l,Token=s)
                        Secu.save()
                        dis = D_Detail(Display_Name=Name)
                        dis.save()
                        mes = {
                        'message':'Login Successful!!',
                        'Token':s
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


def Doctor_dash(request):
        if request.method == 'POST':
        
             data = json.loads(request.body)     
             Token_d = data['Token']

             if (D_Security.objects.filter(Token = Token_d).exists()):
               Receptionist_s  =D_Security.objects.filter(Token = Token_d)[0]
               Username_d      = Receptionist_s.Username
               Doctor_li         = D_Detail.objects.filter(Username = Username_d)
               Doctor_det        = list(Doctor_li.values('id','First_Name','Last_Name','Username','DOB','Email','Mobile_Number','Gender','Government_ID','Gov_ID_Number','Height','Weight','Appointment_fees','Blood_Group','Qualification','Speciality','Experience','Previously_Working_at','Address','City','State','Country','Pincode'))[0]
              
               mes = {      
                    'Doctor_detail'  :Doctor_det,
                    }
               return JsonResponse(mes,status=200,safe=False)
             else:   
               mes = {
                        'message':'Invalid Login attempt!'
                     }
               return JsonResponse(mes,status=403,safe=False)


def Doctor_Logout(request):
    if request.method == 'POST':
        data = json.loads(request.body)     
        Token_d = data['Token']               
        Secu = D_Security.objects.get(Token=Token_d)
        Secu.delete()
        mes = {      
        'message'    :"Token Deleted!"
        }
        return JsonResponse(mes,status=200,safe=False)               




def Appointment_Noti(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Token_d = data['Token']
        if (D_Security.objects.filter(Token = Token_d).exists()):
            Doctor_s  =D_Security.objects.filter(Token = Token_d)[0]
            Username_d      = Doctor_s.Username
            User_list = D_Detail.objects.filter(Username = Username_d)[0]
            First_N    = User_list.First_Name
            Last_N     = User_list.Last_Name
            Name       = "Dr." + First_N + " " + Last_N
    
            if (P_Appointment.objects.filter(Appointed_Doctor = Name).exists()):

              Patient_d       = P_Appointment.objects.filter(Appointed_Doctor = Name, Appointment_Status="Waiting For Doctor's Approval",Payment_Status="Successful")
              if(Patient_d):

                 Patient_det= []
                 for i in Patient_d:               
                   
                   Patient_det.append({"ID":i.id,"F_Name":i.Patient.First_Name,"L_Name":i.Patient.Last_Name,"App_date":i.Appointment_date,"App_time":i.Appointment_time,"Pat_disease":i.Patient_Disease,"App_Stat":i.Appointment_Status})

                 mes = {
                          'Appointment_detail' :Patient_det
                       }
                 return JsonResponse(mes,status=200,safe=False)
              else:
                 mes = {
                          'message' :"No Appointment Approval Pending!"
                       }
                 return JsonResponse(mes,status=403,safe=False)                                


def Appointment_St_Up(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        id_d = data['id']
        App_p  = data['Appointment_St']
        
        if(P_Appointment.objects.filter(id = id_d).exists()):
            App = P_Appointment.objects.filter(id = id_d)[0]
            App_s = App.Appointment_Status

            if(App_s=="Waiting For Doctor's Approval"):
                if(App_p=="Accept"):
                    obj = P_Appointment.objects.get(id=id_d)
                    obj.Appointment_Status="Approved"
                    obj.save(update_fields=['Appointment_Status'])
                    mes = { 
                            'message' :'Appointment Fixed Successfully!'
                             }
                    return JsonResponse(mes,status=200,safe=False)
                if(App_p=="Reject"):
                    App_rej = data['Reason']
                    if (not App_rej):
                      mes = {
                    'message': 'Rejection Reason Required!!'
                        }
                      return JsonResponse(mes,status=403,safe=False)
                    obj = P_Appointment.objects.get(id=id_d)
                    obj.Appointment_Status="Rejected"
                    obj.App_Rej_Reason=App_rej
                    obj.save(update_fields=['Appointment_Status','App_Rej_Reason'])
                    mes = { 
                            'message' :'Appointment Rejected!'
                             }
                    return JsonResponse(mes,status=200,safe=False)


def Appointments(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Token_d = data['Token']
        if (D_Security.objects.filter(Token = Token_d).exists()):
            Doctor_s  =D_Security.objects.filter(Token = Token_d)[0]
            Username_d      = Doctor_s.Username


            Doctor_list = D_Detail.objects.filter(Username = Username_d)[0]
            Name = Doctor_list.Display_Name
    
            if (P_Appointment.objects.filter(Appointed_Doctor = Name).exists()):

              Patient_d       = P_Appointment.objects.filter(Appointed_Doctor = Name, Appointment_Status="Approved",Payment_Status="Successful")
              if(Patient_d):

                 Patient_det= []
                 for i in Patient_d:               
                   
                   Patient_det.append({"ID":i.id,"F_Name":i.Patient.First_Name,"L_Name":i.Patient.Last_Name,"Usern":i.Patient.Username,"email":i.Patient.Email,"M_No":i.Patient.Mobile_Number,"Gen":i.Patient.Gender,"App_date":i.Appointment_date,"App_time":i.Appointment_time,"Pat_disease":i.Patient_Disease,"Pat_Age":i.Patient_Age,"Pres":i.Prescription})

                 
    
                 mes = {
                          'Appointment_detail' :Patient_det
                       }
                 return JsonResponse(mes,status=200,safe=False)
              else:
                 mes = {
                          'message' :"No Upcoming Appointment!"
                       }
                 return JsonResponse(mes,status=403,safe=False)




def Add_Appointment_d(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Token_d = data['Token']
        if (D_Security.objects.filter(Token = Token_d).exists()):
            Doctor_s  =D_Security.objects.filter(Token = Token_d)[0]
            Username_d      = Doctor_s.Username
            Doctor_list = D_Detail.objects.filter(Username = Username_d)[0]
            Name       = Doctor_list.Display_Name
    
            if (P_Appointment.objects.filter(Appointed_Doctor = Name).exists()):
                 Patient_d       = P_Appointment.objects.filter(Appointed_Doctor = Name)

                 Patient_det= []
                 for i in Patient_d:               
                   
                   Patient_det.append({"Id":i.Patient.id,"F_Name":i.Patient.First_Name,"L_Name":i.Patient.Last_Name})

                 mes = {
                          'Appointment_detail' :Patient_det
                       }
                 return JsonResponse(mes,status=200,safe=False)
            else:
                 mes = {
                          'Appointment_detail' :"No Patient Registered!"
                       }
                 return JsonResponse(mes,status=200,safe=False)


def Patient_Gender(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_d = data['id']

        Pat= P_Detail.objects.filter(id=id_d)
        Doctor_det        = list(Pat.values('id','Gender'))[0]
        mes = {
                  'Patient_gender' :Doctor_det
              }
        return JsonResponse(mes,status=200,safe=False)                 


def Add_Appointment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Patient_Age_l      = data['Patient_Age']
        Patient_Disease_l  = data['Patient_Disease']
        Appointed_Doctor_l = data['Appointed_Doctor']
        Appointment_date_l = data['Appointment_date']
        Appointment_time_l = data['Appointment_time']
        id_p               = data['id']

        
        if (P_Detail.objects.filter(id = id_p).exists()):
            
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
             x = datetime.datetime.now()
             new_appointment = P_Appointment(Patient=Patient_l,Patient_Age=Patient_Age_l, Patient_Disease=Patient_Disease_l, Appointment_date=Appointment_date_l,Appointment_time=Appointment_time_l,Appointed_Doctor=Appointed_Doctor_l,Appointment_Status="Approved",Payment_Status="Successful",Payment_Time=x)
             new_appointment.save() 
             mes = { 
                  'message'   :'Appointment Fixed!!'
                  }
             return JsonResponse(mes,status=200,safe=False)

        else:
                 mes = {
                          'message' :"Invalid Appointment Booking!"
                       }
                 return JsonResponse(mes,status=200,safe=False)




def Patient_detail(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Token_d = data['Token']
        if (D_Security.objects.filter(Token = Token_d).exists()):
            Doctor_s  =D_Security.objects.filter(Token = Token_d)[0]
            Username_d      = Doctor_s.Username


            User_list = D_Detail.objects.filter(Username = Username_d)[0]
            First_N    = User_list.First_Name
            Last_N     = User_list.Last_Name
            Name       = "Dr." + First_N + " " + Last_N
    
            if (P_Appointment.objects.filter(Appointed_Doctor = Name).exists()):
                 Patient_d       = P_Appointment.objects.filter(Appointed_Doctor = Name)
                 Patient_det= []
                 for i in Patient_d:               

                   Patient_det.append({"id":i.Patient.id,"F_Name":i.Patient.First_Name,"L_Name":i.Patient.Last_Name,"Usern":i.Patient.Username,"dob":i.Patient.DOB,"email":i.Patient.Email,"M_No":i.Patient.Mobile_Number,"Gend":i.Patient.Gender,"height":i.Patient.Height,"weight":i.Patient.Weight,"blood_group":i.Patient.Blood_Group,"address":i.Patient.Address,"city":i.Patient.City,"state":i.Patient.State,"country":i.Patient.Country})

                 
    
                 mes = {
                          'Patient_detail' :Patient_det
                       }
                 return JsonResponse(mes,status=200,safe=False) 


def Patient_Prescription(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        id_d = data['id']
        Prescription_p  = data['prescription']
        Diagnosis_p     = data['diagnosis']
        if (not Diagnosis_p):
                  mes = {
                    'message': 'Diagnosis Report Required!!'
                   }
                  return JsonResponse(mes,status=403,safe=False)
        if (not Prescription_p):
                  mes = {
                    'message': 'Patient Prescription Required!!'
                   }
                  return JsonResponse(mes,status=403,safe=False)
        
        if(P_Appointment.objects.filter(id = id_d).exists()):
            App = P_Appointment.objects.filter(id = id_d)[0]
            
            obj = P_Appointment.objects.get(id=id_d)
            obj.Prescription=Prescription_p
            obj.Diagnosis=Diagnosis_p
            obj.Appointment_Status="Visited"

            obj.save(update_fields=['Prescription','Diagnosis','Appointment_Status'])
            mes = { 
                    'message' :'Prescription Saved Successfully!'
                     }
            return JsonResponse(mes,status=200,safe=False)


def Patient_Pres_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_d = data['id']
        Token_d = data['Token']
        if (D_Security.objects.filter(Token = Token_d).exists()):
            Doctor_s  =D_Security.objects.filter(Token = Token_d)[0]
            Username_d      = Doctor_s.Username
            Doctor_li       = D_Detail.objects.filter(Username = Username_d)
            Doctor_det      = list(Doctor_li.values('First_Name','Last_Name','Email','Mobile_Number','Gender','Qualification','Speciality'))[0]

            if(P_Appointment.objects.filter(id = id_d).exists()):
                App = P_Appointment.objects.filter(id = id_d)[0]
                Patient_det= []
                Patient_det.append({"ID":App.id,"F_Name":App.Patient.First_Name,"L_Name":App.Patient.Last_Name,"Usern":App.Patient.Username,"App_date":App.Appointment_date,"Pat_disease":App.Patient_Disease,"Pat_Age":App.Patient_Age,"M_No":App.Patient.Mobile_Number,"Gen":App.Patient.Gender,"email":App.Patient.Email})
                mes = {
                              'Patient_detail' :Patient_det,
                              'Doctor_detail'  :Doctor_det 
                           }
                return JsonResponse(mes,status=200,safe=False)





def Previous_Appointment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Token_d = data['Token']
        if (D_Security.objects.filter(Token = Token_d).exists()):
            Doctor_s  =D_Security.objects.filter(Token = Token_d)[0]
            Username_d      = Doctor_s.Username


            Doctor_list = D_Detail.objects.filter(Username = Username_d)[0]
            Name = Doctor_list.Display_Name
    
            if (P_Appointment.objects.filter(Appointed_Doctor = Name).exists()):

              Patient_d       = P_Appointment.objects.filter(Appointed_Doctor = Name, Appointment_Status="Visited")
              if(Patient_d):

                 Patient_det= []
                 for i in Patient_d:               
                   
                   Patient_det.append({"ID":i.id,"F_Name":i.Patient.First_Name,"L_Name":i.Patient.Last_Name,"Usern":i.Patient.Username,"email":i.Patient.Email,"M_No":i.Patient.Mobile_Number,"Gen":i.Patient.Gender,"App_date":i.Appointment_date,"App_time":i.Appointment_time,"Pat_disease":i.Patient_Disease,"Med_History":i.Medical_History,"Pat_Age":i.Patient_Age,"Pres":i.Prescription})

                 
    
                 mes = {
                          'Appointment_detail' :Patient_det
                       }
                 return JsonResponse(mes,status=200,safe=False)
              else:
                 mes = {
                          'Appointment_detail' :"No Upcoming Appointment!"
                       }
                 return JsonResponse(mes,status=200,safe=False)



def Prescription_view(request):
     if request.method == 'POST':
        data = json.loads(request.body)
        id_d = data['id']


        App = P_Appointment.objects.filter(id = id_d,Appointment_Status="Visited")[0]
        App_Doctor = App.Appointed_Doctor
        Doc = D_Detail.objects.filter(Display_Name=App_Doctor)[0]

        Patient_det= []
        Patient_det.append({"F_Name":App.Patient.First_Name,"L_Name":App.Patient.Last_Name,"User":App.Patient.Username,"App_date":App.Appointment_date,"Pat_disease":App.Patient_Disease,"Pat_Age":App.Patient_Age,"Gen":App.Patient.Gender,"Diag":App.Diagnosis,"Pres":App.Prescription,"App_Doc":App_Doctor,"Doc_Quali":Doc.Qualification,"Doc_Spec":Doc.Speciality,"Doc_Email":Doc.Email,"Doc_Mobile":Doc.Mobile_Number})              
        mes = {
                'Patient_detail' :Patient_det, 
              }
        return JsonResponse(mes,status=200,safe=False) 




def Specialization_reg(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Speci =data['Specialization']

        new_speci = D_Specialization(Specialization=Speci)
        new_speci.save()
        mes = {
                  'message' :"Specialization added Successfully!"
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





                               





        
        


      

    
        