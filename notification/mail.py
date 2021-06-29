import requests
from app.models import *
from datetime import date,datetime
from django.core.mail import send_mail
from django.conf import settings

def search():
    user = User.objects.all()
    today = datetime.today().strftime('%d-%m-%Y')
    print(today)
    for i in user:
        print(i.email)
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(i.pin,today)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r = requests.get(URL,headers=headers)
        print(r)
        data = r.json()
        centers = data['centers']
        for center in centers:
            for session in center["sessions"]:
                if session["min_age_limit"] <= i.age:
                    if session["available_capacity"] > 0:
                        subject = 'Covid-Vaccine availability'
                        message = "\t {}\n\t {}\n\t Time: {} To {}\n\t Price: {}\n\t Available Capacity: {}\n\t Vaccine: {}".format(center["name"],center['address'],center["from"],center["to"],center["fee_type"],session["available_capacity"],session["vaccine"])
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [i.email, ]
                        send_mail( subject, message, email_from, recipient_list )

                        print("\t", center["name"])
                        print("\t", center["address"])
                        print("\t Time: ", center["from"]+" TO "+center["to"])
                        print("\t Price: ", center["fee_type"])
                        print("\t Available Capacity: ", session["available_capacity"])
                        if(session["vaccine"] != ''):
                            print("\t Vaccine: ", session["vaccine"])
                        print("\n\n")
                    else:
                        print("No slot available right now")