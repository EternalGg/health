from django.urls import path
from . import views

urlpatterns = [
    path(r'resume/', views.resume_view),
    path('doctor/<str:did>', views.doctorinfo_view)
]