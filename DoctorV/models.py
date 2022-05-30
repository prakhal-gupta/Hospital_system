from django.db import models

class D_Detail(models.Model):
        First_Name             = models.CharField(max_length=50, null=True)
        Last_Name              = models.CharField(max_length=50, null=True)
        Display_Name           = models.CharField(max_length=50, null=True)
        Username               = models.CharField(max_length=50, null=True)
        DOB                    = models.DateField(max_length=50,null=True)
        Email                  = models.EmailField(null=True)
        Password               = models.CharField(max_length=120, null=True)
        Mobile_Number          = models.CharField(max_length=10, null=True)
        Gender                 = models.CharField(max_length=20, null=True)
        Government_ID          = models.CharField(max_length=50, null=True)
        Gov_ID_Number          = models.CharField(max_length=50, null=True)
        Height                 = models.CharField(max_length=20, null=True)
        Weight                 = models.CharField(max_length=20, null=True)
        Appointment_fees       = models.IntegerField(null=True)
        Blood_Group            = models.CharField(max_length=10, null=True)
        Qualification          = models.CharField(max_length=50, null=True)
        Speciality             = models.CharField(max_length=50, null=True)
        Experience             = models.CharField(max_length=120, null=True)
        Previously_Working_at  = models.CharField(max_length=120, null=True)
        Address                = models.CharField(max_length=50, null=True)
        City                   = models.CharField(max_length=50, null=True)
        State                  = models.CharField(max_length=50, null=True)
        Country                = models.CharField(max_length=50, null=True)   
        Pincode                = models.CharField(max_length=20, null=True)
        # Profile_pic            = models.ImageField(upload_to='Doctor/Profile_pic/',null=True,blank=True)
        Registered_at          = models.DateTimeField(auto_now_add=True, null=True)

class D_Security(models.Model):
     Doctor                = models.ForeignKey(D_Detail,on_delete=models.CASCADE)
     Username              = models.CharField(max_length=50,null=True)
     Token                 = models.CharField(max_length=30, null=True) 
     Generated_at          = models.DateTimeField(auto_now_add=True, null=True)

class D_Specialization(models.Model):
            Specialization = models.CharField(max_length=50,null=True)        
