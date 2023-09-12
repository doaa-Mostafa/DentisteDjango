
from django.urls import path
from .views import *

urlpatterns = [
   path('',home,name="home"),
   path('contact/',contact,name="contact"),
   path('doctors/',doctors,name="doctors"),
   path('pricing/',pricing,name="pricing"),
   path('num-teeth/',teeth,name="num-teeth"),
   path('about/',about,name="about"),
   path('appointment/',appointment,name="appointment"),
   path('admin_login/', Login,name="login"),
   path('logout/',Logout_admin,name="logout"),
   path('index/',Index,name="index"),
   path('view_doctor/', View_Doctor, name="view_doctor"),
   path('add_doctor/', Add_Doctor, name="add_doctor"),
   path('delete_doctor(?P<int:pid>)', Delete_Doctor, name="delete_doctor"),
   path('view_patient/', View_Patient, name="view_patient"),
   path('add_patient/', Add_Patient, name="add_patient"),
   path('delete_patient(?P<int:pid>)', Delete_Patient, name="delete_patient"),
   path('view_appoinment/', View_Appoinment, name="view_appoinment"),
   path('add_appoinment/', Add_Appoinment, name="add_appoinment"),
   path('delete_appoinment(?P<int:pid>)', Delete_Appoinment, name="delete_appoinment"),
  

]
