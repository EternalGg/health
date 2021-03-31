from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import json
from .models import chat as chats
from django.utils import timezone
from Info.models import *
import time
from User.models import *

# Create your views here.
def chat(request):
    username = request.session.get('username')
    userid = user.objects.get(u_account=username).id
    userinfos = userinfo.objects.filter(u_account=username).last()
    doctor = doctorinfo.objects.get(d_department=userinfos.d_department)
    appointments = appointment.objects.get(u_id=userid,is_done=0)
    appointments.opentime = timezone.localtime(timezone.now())
    appointments.is_working = True
    appointments.save()
    data = {'id': appointments.id, 'time': appointments.opentime, 'doctor_name': doctor.d_name,
            'reason': userinfos.u_description, 'department': userinfos.d_department,
            'doctor_id': doctor.id, 'age': userinfos.u_age, 'gender': userinfos.u_gender, 'name': userinfos.u_name }
    return render(request, 'chat.html',{"list": data})


def push_message(request):
    data = json.loads(request.body)
    appointmentid = data["appointmentid"]
    username = data["master"]
    message = data["message"]
    flag = data["flag"]
    plus_message = chats.objects.create(appointment_id=appointmentid, master=username, message=message, flag=flag)
    return HttpResponse(request.body)


def get_message(request):
    data = json.loads(request.body)
    appointmentid = data["appointmentid"]
    other_side = data["otherside"]
    flag = data["cflag"]
    flag = flag - 1
    print(flag)
    check_new_message = chats.objects.filter(appointment_id=appointmentid, master=other_side).count()
    if flag != check_new_message:
        new_message = chats.objects.get(appointment_id=appointmentid, master=other_side, flag=flag)
        flag = flag + 1
        data = {'newmessage': new_message.message, 'flag': flag}
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')


def dochat(request,aid):
    return render(request, 'dochat.html',{'id':aid})
