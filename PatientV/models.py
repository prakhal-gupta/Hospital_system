from django.db import models

class P_Detail(models.Model):
        First_Name          = models.CharField(max_length=50, null=True)
        Last_Name           = models.CharField(max_length=50, null=True)
        Username            = models.CharField(max_length=50,null=True)
        DOB                 = models.DateField(null=True)
        Email               = models.EmailField(null=True)
        Password            = models.CharField(max_length=120, null=True)
        Mobile_Number       = models.CharField(max_length=10, null=True)
        Gender              = models.CharField(max_length=20, null=True)
        Government_ID       = models.CharField(max_length=50, null=True)
        Gov_ID_Number       = models.CharField(max_length=50, null=True)
        Height              = models.CharField(max_length=20, null=True)
        Weight              = models.CharField(max_length=20, null=True)
        Blood_Group         = models.CharField(max_length=10, null=True)
        Patient_Age         = models.CharField(max_length=5, null=True)
        Medical_History     = models.CharField(max_length=250, default="No Medical History")
        Address             = models.CharField(max_length=50, null=True)
        City                = models.CharField(max_length=50, null=True)
        State               = models.CharField(max_length=50, null=True)
        Country             = models.CharField(max_length=50, null=True)   
        Pincode             = models.CharField(max_length=20, null=True)
        Registered_at       = models.DateTimeField(auto_now_add=True, null=True)
        modified_at         = models.DateTimeField(null=True)

        
        
        
class P_Appointment(models.Model):
        Patient               = models.ForeignKey(P_Detail,on_delete=models.CASCADE)        
        Payment_Status        = models.CharField(max_length=50,default="Pending")
        Payment_Time          = models.DateTimeField(null=True)
        Patient_Disease       = models.CharField(max_length=120, null=True)
        Appointment_Status    = models.CharField(max_length=50,default="Pending")
        Appointment_date      = models.DateField(null=True)
        Appointment_time      = models.CharField(max_length=50, null=True)
        Appointed_Doctor      = models.CharField(max_length=50, null=True)
        Diagnosis             = models.CharField(max_length=250, null=True)
        Prescription          = models.CharField(max_length=250, null=True)
        App_Rej_Reason        = models.CharField(max_length=50,default="Not Rejected")
        Appointment_reg_at    = models.DateTimeField(auto_now_add=True, null=True)
        Appointment_mod_at    = models.DateTimeField(null=True)




class P_Security(models.Model):
     Patient               = models.ForeignKey(P_Detail,on_delete=models.CASCADE)
     Username              = models.CharField(max_length=50,null=True)
     Token                 = models.CharField(max_length=30, null=True) 
     Generated_at          = models.DateTimeField(auto_now_add=True, null=True) 


class P_Disease(models.Model):
        Disease =  models.CharField(max_length=50,null=True)        
