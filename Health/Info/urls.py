from django.urls import path
from . import views

urlpatterns = [
    path(r'resume/', views.resume_view),
    path('doctor/<str:did>', views.doctorinfo_view),
    path(r'user_resume/', views.user_resume_view),
    path(r'end_appointment/<str:id>', views.end_appointment),
    path(r'updateill/', views.updateill),
    path(r'deleteappoint/',views.delete_appointment),
    path(r'subsequent/', views.subsequent),
    path('doctortwo/<str:did>', views.doctorinfo_viewtwo),

]
