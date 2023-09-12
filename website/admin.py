from django.contrib import admin

from django.contrib import admin
from .models import Services, Doctor, Appoinment, Patient

admin.site.register(Services)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appoinment)