"""LibraryManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

admin.site.site_header = "Library Management System"
admin.site.site_title = "Library Management System Portal"
admin.site.index_title = "Welcome to Library Management System Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', include('library.urls')),
    path('studentpage', include('library.urls')),
    path('adminpage', include('library.urls')),
    path('studentview', include('library.urls')),
    path('adminsignup', include('library.urls')),
    path('adminlogin', include('library.urls')),
    path('dashboard', include('library.urls')),
    path('addbook', include('library.urls')),
    path('viewbook', include('library.urls')),
    path('bookedit/<int:pk>', include('library.urls')),
    path('bookdelete/<int:pk>', include('library.urls')),
    path('logout', include('library.urls')),
    path('studentlogin', include('library.urls')),
    path('studentsignup', include('library.urls')),
    path('viewstudent', include('library.urls')),
    path('bookissue', include('library.urls')),
    path('issuedbook', include('library.urls')),
]
