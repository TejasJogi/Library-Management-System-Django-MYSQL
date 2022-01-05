from django.contrib import admin
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.index, name='index'),
    path('studentpage', views.studentpage, name='studentpage'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('studentview', views.studentview, name='studentview'),
    path('adminsignup', views.adminsignup, name='adminsignup'),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html')),
    path('admindash', views.admindash, name='admindash'),
    path('addbook', views.addbook, name='addbook'),
    path('viewbook', views.viewbook, name='viewbook'),
    path('bookedit/<int:pk>', views.bookedit, name='bookedit'),
    path('bookdelete/<int:pk>', views.bookdelete, name='bookdelete'),
    path('logout', LogoutView.as_view(template_name='adminlogin.html')),
]
