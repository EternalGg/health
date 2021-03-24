from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def resume_view(request):
    return render(request, 'resume.html')


def doctorinfo_view(request, did):
    doctors = doctorinfo.objects.get(id=did)
    data = {'id': doctors.id, 'name': doctors.d_name, 'local': doctors.d_local, 'department': doctors.d_department,
            'hospital': doctors.d_hospital, 'phone': doctors.d_phone, 'title': doctors.d_title,
            'experience': doctors.d_experience, 'education': doctors.d_education, 'skills': doctors.d_skills,
            'mooto': doctors.d_mooto}
    return render(request, 'doctor.html', {'list': data})
