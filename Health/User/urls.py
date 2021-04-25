from django.urls import path
from . import views

urlpatterns = [
    path(r'loginorregister/', views.login_page),
    path(r'register/', views.register_view),
    path(r'login/', views.login_view),
    path(r'doctorlogin/', views.doctorlogin_view),
    path(r'doctorlog/', views.doctorlogin),
    path(r'u_center/', views.u_center),
    path(r'updatedoctorinfo/', views.update_doctorInfo),
    path(r'updatedoctorinfo/', views.update_doctor)
]
