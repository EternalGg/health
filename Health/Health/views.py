from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import traceback
import json
# import sys,os
# sys.path.append(os.path.dirname("Info") + os.sep + '../')
from Info.models import *


# Create your views here.

def index(request):
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
                'doctor_id': doctor.id, 'age': userinfos.u_age, 'gender': userinfos.u_gender, 'name': userinfos.u_name,
                'd_title': doctor.d_title, 'd_experience': doctor.d_experience, 'd_skills': doctor.d_skills,
                'queue_up': check_queue_up,'edu':doctor.d_education}
        return render(request, 'index2.html', {"list": data})
        # return JsonResponse(json.dumps(json_list), content_type='application/json',safe=False)
    else:
        return render(request, 'index2.html')