from django.shortcuts import render, redirect
from .models import Services
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout


def home(request):
  return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def pricing(request):
    all_services = Services.objects.all
    return render(request, 'pricing.html', {'all':all_services} )


def doctors(request):
  return render(request, 'doctors.html', {})


def teeth(request):
    return render(request, 'num-teeth.html', {})


def Index(request):
    if not request.user.is_staff:
         return redirect('login')
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appoinment.objects.all()
    d=0
    p=0
    a=0
    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1
    d1 = {'d':d,'p':p,'a':a}
    return render(request, 'index.html',d1)


def Login(request):
    error = ""
    if request.method == 'POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d={'error': error}
    return render(request, 'login.html',d)


def Logout_admin(request):
    if not request.user.is_staff:
         return redirect('login')
    logout(request)
    return redirect('login')




def contact(request):

    if request.method == "POST":
       name = request.POST['name']
       mobile = request.POST['mobile']
       email = request.POST['email']
       text = request.POST['text']

       # send an email
       send_mail(
           name, # subject
           text, # message
           email, # from email
           ['Put Doctor Email Here'], # To Email
           )
        
       return render(request, 'contact.html', {'name' : name })
 
    else:
    	return render(request, 'contact.html', {})
   
def appointment(request):

    if request.method == "POST":

       name = request.POST['name']
       email= request.POST['email']
       mobile= request.POST['mobile']
       time = request.POST['time']
       date = request.POST['date']

       
       # send an email
       appointment ='الأسم: ' + name +'\n'+'الجوال:' + mobile + '\n'+'البريد الألكترونى:' + email +'\n'+ 'الوقت:' + time +'\n'+'التاريخ:' +date

       send_mail(
           'Appointment Request',
           appointment, # subject
           email, # from email
           ['Put Doctor Email  Here'], # To Email
           )
        
       return render(request, 'appointment.html', {
        'name': name,
        'email':email,
        'mobile':mobile,
        'time': time,
        'date': date

         })
 
    else:
        return render(request, 'home.html', {})

# ----------------------------------------------------------------------------------------------------------------------


def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    return render(request,'view_doctor.html',{'doc': doc})

	
def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method =='POST':
        n=request.POST['name']
        c=request.POST['contact']
        sp=request.POST['special']

        try:
            Doctor.objects.create(Name=n,mobile=c,special=sp)
            error = "no"

        except:
            error = "yes"
    d={'error': error}
    return render(request, 'add_doctor.html',d)


def Delete_Doctor(request,pid):

    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()

    return render(request, 'view_patient.html', {'pat': pat})


def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        c = request.POST['contact']


        try:
            Patient.objects.create(name=n, gender=g, mobile=c)
            error = "no"

        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_patient.html', d)


def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')


def View_Appoinment(request):
    if not request.user.is_staff:
        return redirect('login')
    app = Appoinment.objects.all()
    a = {'app': app}
    return render(request, 'view_appoinment.html', a)


def Add_Appoinment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        da = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(doctor_name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appoinment.objects.create(Doctor=doctor, Patient=patient, date=da,time=t)
            error = "no"

        except:
            error = "yes"

    d = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return render(request, 'add_appoinment.html', d)


def Delete_Appoinment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    appoinment = Appoinment.objects.get(id=pid)
    appoinment.delete()
    return redirect('view_appoinment')



