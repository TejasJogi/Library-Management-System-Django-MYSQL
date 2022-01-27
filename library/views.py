from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from . import models, forms
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def index(request):   
    return render(request, 'library/index.html')


def adminauth(user):
    return user.groups.filter(name='ADMIN').exists()


def dashboard(request):
    if adminauth(request.user):
        return render(request, 'library/admindash.html')
    else:
        return render(request, 'library/studentdash.html')

class Admin:

    def adminpage(request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('afterlogin')
        return render(request, 'library/adminpage.html')
    

    def adminsignup(request):
        form = forms.AdminSigup()
        if request.method == 'POST':
            form = forms.AdminSigup(request.POST)
            if form.is_valid():
                user = form.save()
                user.set_password(user.password)
                user.save()
                my_admin_group = Group.objects.get_or_create(name='ADMIN')
                my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
        return render(request, 'library/adminsignup.html', {'form': form})


    def adminlogin(request):
        return render(request, 'library/adminlogin.html')

    @login_required(login_url='adminlogin')
    @user_passes_test(adminauth)
    def addbook(request):
        form = forms.BookForm()
        if request.method == 'POST':
            form = forms.BookForm(request.POST)
            if form.is_valid():
                user = form.save()
                return render(request, 'library/bookadded.html')
        return render(request, 'library/addbook.html', {'form': form})

    @login_required(login_url='adminlogin')
    @user_passes_test(adminauth)
    def viewbook(request):
        books = models.Book.objects.all()
        return render(request, 'library/viewbook.html', {'books': books})

    @login_required(login_url='adminlogin')
    @user_passes_test(adminauth)
    def bookedit(request, pk):
        if not request.user.is_superuser:
            return redirect('index')
        obj = models.Book.objects.get(id=pk)
        form = forms.BookForm(instance=obj)
        if request.method == 'POST':
            form = forms.BookForm(
                data=request.POST, files=request.FILES, instance=obj)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                return redirect('index')
        return render(request, 'library/addbook.html', locals())

    @login_required(login_url='adminlogin')
    @user_passes_test(adminauth)
    def bookdelete(request, pk):
        if not request.user.is_superuser:
            return redirect('index')
        obj = get_object_or_404(models.Book, id=pk)
        obj.delete()
        return redirect('viewbook')


class Student:

    def studentpage(request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('afterlogin')
        return render(request, 'library/studentpage.html')

    @login_required(login_url='studentlogin')
    def studentview(request):
        books = models.Book.objects.all()
        return render(request,'library/studentview.html',{'books': books})

    def studentsignup(request):
        form1=forms.StudentUserForm()
        form2=forms.StudentForm()
        mydict={'form1':form1,'form2':form2}
        if request.method=='POST':
            form1=forms.StudentUserForm(request.POST)
            form2=forms.StudentForm(request.POST)
            if form1.is_valid() and form2.is_valid():
                user=form1.save()
                user.set_password(user.password)
                user.save()
                f2=form2.save(commit=False)
                f2.user=user
                user2=f2.save()
                my_student_group = Group.objects.get_or_create(name='STUDENT')
                my_student_group[0].user_set.add(user)
            return HttpResponseRedirect('studentlogin')
        return render(request,'library/studentsignup.html',context=mydict)

    def studentlogin(request):
        return render(request, 'library/studentlogin.html')