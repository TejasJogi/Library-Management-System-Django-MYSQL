from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from . import models, forms
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import date

# Create your views here.

def index(request):   
    return render(request, 'library/index.html')


def adminauth(user):
    return user.groups.filter(name='ADMIN').exists()


def studentauth(user):
        return user.groups.filter(name='STUDENT').exists()


def dashboard(request):
    if adminauth(request.user):
        return render(request, 'library/admindash.html')
    if studentauth(request.user):
        return render(request, 'library/studentdash.html')

class Admin:

    def adminpage(request):
        return render(request, 'library/adminpage.html')
    

    def adminsignup(request):
        form = forms.UserForm()
        if request.method == 'POST':
            form = forms.UserForm(request.POST)
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
        if not request.user.is_active:
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
        if not request.user.is_active:
            return redirect('index')
        obj = get_object_or_404(models.Book, id=pk)
        obj.delete()
        return redirect('viewbook')

    @login_required(login_url='adminlogin')
    @user_passes_test(adminauth)
    def viewstudent(request):
        students=models.Student.objects.all()
        return render(request,'library/viewstudent.html',{'students':students})

    @login_required(login_url='adminlogin')
    @user_passes_test(adminauth)
    def bookissue(request):
        form=forms.BookissueForm()
        if request.method=='POST':
            form=forms.BookissueForm(request.POST)
            if form.is_valid():
                obj=models.Bookissued()
                obj.branch=request.POST.get('branch2')
                obj.isbn=request.POST.get('isbn2')
                obj.save()
                return render(request,'library/bookissued.html')
        return render(request,'library/bookissue.html',{'form':form})

    @login_required(login_url='adminlogin')
    @user_passes_test(adminauth)
    def issuedbook(request):
        issuedbooks=models.Bookissued.objects.all()
        li=[]
        for ib in issuedbooks:
            issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
            expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)

            days=(date.today()-ib.issuedate)
            print(date.today())
            d=days.days
            fine=0
            if d>15:
                day=d-15
                fine=day*10
            books=list(models.Book.objects.filter(isbn=ib.isbn))
            students=list(models.Student.objects.filter(id=ib.id))
            i=0
            for l in books:
                t=(students[i].fullname,students[i].rolldiv,books[i].name,books[i].author,issdate,expdate,fine)
                print(t)
                i=i+1
                li.append(t)
        return render(request,'library/issuedbook.html',{'li':li})


class Student:

    def studentpage(request):
        return render(request, 'library/studentpage.html')

    def studentlogin(request):
        return render(request, 'library/studentlogin.html')


    @login_required(login_url='studentlogin')
    @user_passes_test(studentauth)
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

        