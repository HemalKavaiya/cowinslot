from django.shortcuts import render,redirect
from django.contrib import messages
import requests
import json
from csv import DictWriter
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from django.views.decorators.csrf import csrf_exempt
from datetime import date,datetime
import urllib.request,urllib.parse,threading
from urllib.request import Request,urlopen
from datetime import datetime

def home(request):
    return render(request,'index.html')

@csrf_exempt
def userdata(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        pin = request.POST.get("pin")
        age = int(request.POST.get("age"))

        try:
            User.objects.get(email=email)
            messages.error(request,"Email already exists")    
            return redirect('home')
        except:
            user = User(name=name,email=email,pin=pin,age=age).save()
            
            users = {
                'Name':name,
                'Email':email,
                'Pin':pin,
                'Age':age,
            }
    
            with open('C:/Users/HK/djangoprojects/appointment/users.csv', 'a') as f_object:
                dictwriter_object = DictWriter(f_object, fieldnames=['Name','Email','Pin','Age'])
                dictwriter_object.writerow(users)
                f_object.close()
        
            messages.success(request,"You will get notified whenever there is slot available")    
            return redirect('home')
    return redirect('home')


def center(request):
    return render(request,'center.html')

def findcenter(request):
    if request.method == "POST":
        pin = request.POST.get('pin')
        today = datetime.today().strftime('%d-%m-%Y')
        print(today)
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pin,today)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r = requests.get(URL,headers=headers)
        print(r)

        if r.status_code == 200:
            data = r.json()
            centers = data['centers']

            con={}            

            count = int(1)

            for center in centers:

                name = str(center['name'])
                add = str(center['address'])
                dist = str(center['district_name'])
                state = str(center['state_name'])
                pin = str(center['pincode'])
                frm = str(center['from'])
                to = str(center['to'])
                fee = str(center['fee_type'])

                con[count] = "Name : "+name+"\nAddress : "+add+", "+dist+", "+state+" "+pin+"\nTime : "+frm+" To "+to+"\nFee : "+fee 
                
                count += 1
        
            if con:
                return render(request,'center.html',{'con':con})
            else:
                messages.error(request,"Can not reach server at the moment please try again after some time")
                return redirect('center')
        else:
            messages.error(request,"Can not reach server at the moment please try again after some time")
            return redirect('center')
    return redirect('center')
    





# for i in range(1,len(con.keys())+1):
#     for j in range(len(con[i])):
#         for x in range(i,6):
#             print(con[x][j])
        
#     print('\n')
#     break


