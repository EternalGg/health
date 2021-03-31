from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import traceback
import json
# import sys,os
# sys.path.append(os.path.dirname("Info") + os.sep + '../')
from Info.models import *
from User.models import *

# Create your views here.

def index(request):
    username = request.session.get('username')

    flag = userinfo.objects.filter(u_account=username)
    if flag:
        userid = user.objects.get(u_account=username).id
        # 查询appointment是否创建
        infoid = userinfo.objects.filter(u_account=username).last()
        flag1 = userinfo.objects.filter(u_account=username).count()
        flag2 = appointment.objects.filter(info_id=infoid.id)
        doctor = doctorinfo.objects.get(d_department=infoid.d_department)
        if flag2:
            pass
        else:
            make_appointment = appointment.objects.create(d_department=infoid.d_department, info_id=infoid.id,
                                                          d_id=doctor.id,u_id=userid)
        is_done = appointment.objects.filter(u_id=userid, is_done=0).count()
        have_done = appointment.objects.filter(u_id=userid, is_done=1).count()

        check_queue_up = appointment.objects.filter(d_department=infoid.d_department, is_done=0).count()
        data = {'doctor_name': doctor.d_name, 'reason': infoid.u_description, 'department': infoid.d_department,
                'doctor_id': doctor.id, 'age': infoid.u_age, 'gender': infoid.u_gender, 'name': infoid.u_name,
                'd_title': doctor.d_title, 'd_experience': doctor.d_experience, 'd_skills': doctor.d_skills,
                'queue_up': check_queue_up,'edu':doctor.d_education,'is_done':is_done,'have_done':have_done}
        return render(request, 'index2.html', {"list": data})
        # return JsonResponse(json.dumps(json_list), content_type='application/json',safe=False)
    else:
        return render(request, 'index2.html')