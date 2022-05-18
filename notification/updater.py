from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from notification import mail

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(mail.search, 'interval', minutes=1440)
    scheduler.start()