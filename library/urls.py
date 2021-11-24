from django.contrib import admin
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.index, name='index'),
    path('studentpage', views.studentpage, name='studentpage'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('studentview', views.studentview, name='studentview'),
    path('adminsignup', views.adminsignup, name='adminsignup'),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html')),
    
]
