from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeModalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile',
     'email', 'job_city', 'profile_image', 'myfile']

# Register your models here.
