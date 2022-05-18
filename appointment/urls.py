from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('userdata',userdata, name="userdata"),
    path('center',center, name="center"),
    path('findcenter',findcenter, name="findcenter"),
    path('unsubscribe',unsubscribe, name="unsubscribe"),

]
