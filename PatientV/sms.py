# from twilio.rest import Client
# import string
# import random
# from PatientV.models import P_Detail,P_Security






# def sms_view(User_l):
#          account_sid = 'ACac9e10c75b68150788fc1089bfdd36c3'
#          auth_token = '58f298e22b32b361359d3990311edd9d'
#          client = Client(account_sid, auth_token)
#          a=list((string.digits))
#          s=""
#          for i in range(6):
#           b=random.choice(a)
#           s+=b
          
#          if (P_Detail.objects.filter(Username = User_l).exists()):
#              Patient_d = P_Detail.objects.filter(Username = User_l)[0]
#              Mobile = Patient_d.Mobile_Number
#              x=P_Detail.objects.get(Username=User_l)
#              Secu = P_Security(Patient=x,Username=User_l,OTP=s)
#              Secu.save()
              
                    

#              message = client.messages.create(
#                       body='Your OTP to reset Password is :'+ s,
#                       from_='+16203191278',
#                        to= '+91' + Mobile
#                       )                   