from django.urls import path
from library import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.index, name='index'),
    path('studentpage', views.Student.studentpage, name='studentpage'),
    path('adminpage', views.Admin.adminpage, name='adminpage'),
    path('studentview', views.Student.studentview, name='studentview'),
    path('adminsignup', views.Admin.adminsignup, name='adminsignup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('addbook', views.Admin.addbook, name='addbook'),
    path('viewbook', views.Admin.viewbook, name='viewbook'),
    path('bookedit/<int:pk>', views.Admin.bookedit, name='bookedit'),
    path('bookdelete/<int:pk>', views.Admin.bookdelete, name='bookdelete'),
    path('logout', LogoutView.as_view(template_name='library/index.html'), name="logout"),
    # path('login', views.login, name="login"),
    path('studentsignup', views.Student.studentsignup, name='studentsignup'),
    path('viewstudent', views.Admin.viewstudent, name='viewstudent'),
    path('bookissue', views.Admin.bookissue, name='bookissue'),
    path('issuedbook', views.Admin.issuedbook, name='issuedbook'),
    path('studentissuedbook', views.Student.studentissuedbook, name='studentissuedbook'),
    path('change_password', views.changepassword, name='changepassword'),
    path('reset_password', views.resetpassword, name='resetpassword'),
    path('api/users', views.UserList.as_view()),
    path('api/users/<int:pk>', views.UserDetail.as_view()),
]