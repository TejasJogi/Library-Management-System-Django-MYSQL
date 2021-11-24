from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path('',views.index, name='index'),
    path('studentpage', views.studentpage, name='studentpage'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('studentview', views.studentview, name='studentview'),
    path('adminsignup', views.studentview, name='adminsignup'),
]
