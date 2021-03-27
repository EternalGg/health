from django.urls import path
from . import views

urlpatterns = [
    path(r'resume/', views.resume_view),
    path('doctor/<str:did>', views.doctorinfo_view),
    path(r'user_resume/', views.user_resume_view)
]
