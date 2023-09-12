from django.db import models

class Services(models.Model):
  service = models.CharField(max_length=200)
  price = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  

class Doctor(models.Model):
   doctor_name = models.CharField(max_length=50)
   mobile = models.IntegerField()
   special = models.CharField(max_length=50)

   def __str__(self):
    return self.doctor_name

class Patient (models.Model):
  name= models.CharField(max_length=50)
  gender = models.CharField(max_length=10)
  mobile = models.IntegerField(null=True)
  address = models.CharField(max_length=150)

  def __str__(self):
    return self.name

class Appoinment(models.Model):
  Doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
  Patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
  date = models.DateField()
  time = models.TimeField()


  def __str__(self):
    return self.doctor.name+"--"+self.patient.name

 