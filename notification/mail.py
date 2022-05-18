import requests
from app.models import *
from datetime import date,datetime
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def search():
    
    user = User.objects.filter(status = 1)
    today = datetime.today().strftime('%d-%m-%Y')
    print(today)
    mySession = requests.Session()
    for i in user:
        print(i.email)
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(i.pin,today)
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        # print(headers)
        link = "https://cowinslot.herokuapp.com/unsubscribe?email="+i.email
        r = mySession.get(URL,headers=headers)
        print(r)
        if r.status_code == 200:
            data = r.json()
            centers = data['centers']
            for center in centers:
                for session in center["sessions"]:
                    if session["min_age_limit"] <= i.age:
                        if session["available_capacity"] > 0:
                            subject = 'Covid-Vaccine availability'
                            # message = "<p>{}</p><p>{}</p><p>Time: {} To {}</p><p>Price: {}</p><p>Available Capacity: {}</p><p>Vaccine: {}</p>".format(center["name"],center['address'],center["from"],center["to"],center["fee_type"],session["available_capacity"],session["vaccine"])
                            message = "\t {}\n\t {}\n\t Time: {} To {}\n\t Price: {}\n\t Available Capacity: {}\n\t Vaccine: {}\n\t To stop receiving notification click {} \n\t You can activate it again by simplly registrating yourself again".format(center["name"],center['address'],center["from"],center["to"],center["fee_type"],session["available_capacity"],session["vaccine"],link)
                            email_from = settings.EMAIL_HOST_USER
                            recipient_list = [i.email, ]
                            send_mail( subject, message, email_from, recipient_list )

                            # if(session["vaccine"] != ''):
                            #     print("\t Vaccine: ", session["vaccine"])
                            # print("\n\n")
                        else:
                            continue