from django.urls import path
from library import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.index, name='index'),
    path('studentpage', views.Student.studentpage, name='studentpage'),
    path('adminpage', views.Admin.adminpage, name='adminpage'),
    path('studentview', views.Student.studentview, name='studentview'),
    path('adminsignup', views.Admin.adminsignup, name='adminsignup'),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html'), name="login"),
    path('admindash', views.Admin.admindash, name='admindash'),
    path('addbook', views.Admin.addbook, name='addbook'),
    path('viewbook', views.Admin.viewbook, name='viewbook'),
    path('bookedit/<int:pk>', views.Admin.bookedit, name='bookedit'),
    path('bookdelete/<int:pk>', views.Admin.bookdelete, name='bookdelete'),
    path('logout', LogoutView.as_view(template_name='adminlogin.html'), name="logout"),
    path('studentlogin', LoginView.as_view(template_name='studentlogin.html'), name="login"),
    path('studentsignup', views.Student.studentsignup, name='studentsignup'),
]
