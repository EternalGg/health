from django.urls import path
from . import views

urlpatterns = [
    path(r'chat/', views.chat),
    path(r'dochat/<str:aid>', views.dochat),
    path(r'push/', views.push_message),
    path(r'pull/', views.get_message),

]
