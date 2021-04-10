from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from django.shortcuts import redirect

# 信息输入
def resume_view(request):
    username = request.session.get('username')
    return render(request, 'resume.html', {"username": username})


# 医生信息
def doctorinfo_view(request, did):
    doctors = doctorinfo.objects.get(id=did)
    data = {'id': doctors.id, 'name': doctors.d_name,
            'local': doctors.d_local, 'department': doctors.d_department,
            'hospital': doctors.d_hospital, 'phone': doctors.d_phone,
            'title': doctors.d_title,
            'experience': doctors.d_experience,
            'education': doctors.d_education, 'skills': doctors.d_skills,
            'mooto': doctors.d_mooto}
    return render(request, 'doctor.html', {'list': data})


# 用户挂号信息
def user_resume_view(request):
    username = request.session.get('username')
    realname = request.POST.get('realname')
    phone = request.POST.get('phone')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    department = request.POST.get('department')
    desc = request.POST.get('desc')
    resume = userinfo.objects.create(u_account=username, u_name=realname,
                                     u_age=age, u_gender=gender,
                                     d_department=department,
                                     u_description=desc, u_phone=phone)

    return render(request, 'resume.html', {'flag': True})


def check_is_apointment(request):
    username = request.session.get('username')
    # 查询是否有用户信息
    flag = userinfo.objects.filter(u_account=username)
    if flag:
        # 查询appointment是否创建
        infoid = userinfo.objects.get(u_account=username)
        flag2 = appointment.objects.filter(info_id=infoid.id)
        userinfos = userinfo.objects.get(u_account=username)
        doctor = doctorinfo.objects.get(d_department=userinfos.d_department)
        if flag2:
            pass
        else:
            make_appointment = appointment.objects.create(d_department=userinfos.d_department, info_id=userinfos.id,
                                                          d_id=doctor.id)

        check_queue_up = appointment.objects.filter(d_department=userinfos.d_department, is_done=0).count()
        data = {'doctor_name': doctor.d_name, 'reason': userinfos.u_description, 'department': userinfos.d_department,
                'doctor_id': doctor.id,'age':userinfos.u_age,'gender':userinfos.u_gender,'name':userinfos.u_name,
                'd_title': doctor.d_title, 'd_experience': doctor.d_experience, 'd_skills': doctor.d_skills,
                'queue_up': check_queue_up}
        return data
        # return JsonResponse(json.dumps(json_list), content_type='application/json',safe=False)
    else:
        return False

def end_appointment(request,id):
    appointments = appointment.objects.get(id=id)
    appointments.is_done = True
    appointments.done_time = timezone.localtime(timezone.now())
    appointments.is_working = False
    appointments.save()
    return HttpResponseRedirect('/')


def updateill(request):
    ill = request.POST.get('ill')
    id = request.POST.get('info_id')
    print(id)
    change = appointment.objects.get(info_id=id)
    change.ill = ill
    change.save()
    return HttpResponse("done!")
