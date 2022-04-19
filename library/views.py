import email
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from . import models, forms, serializers
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import date
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404


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
    else:
        return redirect('/accounts/login/')

# def login(request):
#     form = AuthenticationForm()
#     return render(request, 'account/login.html', {'form':form})


def changepassword(request):
    # form = PasswordChangeForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, form.user)
                messages.success(
                    request, 'Your password was successfully updated!')
                return HttpResponseRedirect('dashboard')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'account/password_change.html', {'form': form})
    else:
        return HttpResponseRedirect('changepassword')


def resetpassword(request):
    # form = SetPasswordForm()
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, form.user)
            messages.success(
                request, 'Your password was successfully updated!')
            return HttpResponseRedirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'account/password_reset.html', {'form': form})


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
        students = models.Student.objects.all()
        return render(request, 'library/viewstudent.html', {'students': students})

    @login_required(login_url='adminlogin')
    @user_passes_test(adminauth)
    def bookissue(request):
        form = forms.BookissueForm()
        if request.method == 'POST':
            form = forms.BookissueForm(request.POST)
            if form.is_valid():
                obj = models.IssuedBook()
                obj.branch = request.POST.get('branch2')
                obj.isbn = request.POST.get('isbn2')
                obj.save()
                return render(request, 'library/bookissued.html')
        # (students[i].fullname, students[i].rolldiv, books[i].name, books[i].author, issdate, expdate, fine)
        return render(request, 'library/bookissue.html', {'form': form})

    @login_required(login_url='adminlogin')
    @user_passes_test(adminauth)
    def issuedbook(request):
        issuedbooks = models.IssuedBook.objects.all()
        li = []
        for ib in issuedbooks:
            issdate = str(ib.issuedate.day)+'-' + \
                str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
            expdate = str(ib.expirydate.day)+'-' + \
                str(ib.expirydate.month)+'-'+str(ib.expirydate.year)

            days = (date.today()-ib.issuedate)
            print(date.today())
            d = days.days
            fine = 0
            if d > 15:
                day = d-15
                fine = day*10

            books = list(models.Book.objects.filter(isbn=ib.isbn))
            print(books)
            students = list(models.Student.objects.filter(id=ib.id))
            print(students)
            i = 0
            for l in books:
                t = (students[i].fullname, students[i].rolldiv, books[i].name, books[i].author, issdate, expdate, fine)
                print(t)
                i = i + 1
                li.append(t)
        return render(request, 'library/issuedbook.html', {'li': li})


class Student:

    def studentpage(request):
        return render(request, 'library/studentpage.html')

    @login_required(login_url='studentlogin')
    @user_passes_test(studentauth)
    def studentview(request):
        books = models.Book.objects.all()
        return render(request, 'library/studentview.html', {'books': books})

    def studentsignup(request):
        form1 = forms.StudentUserForm()
        form2 = forms.StudentForm()
        mydict = {'form1': form1, 'form2': form2}
        if request.method == 'POST':
            form1 = forms.StudentUserForm(request.POST)
            form2 = forms.StudentForm(request.POST)
            if form1.is_valid() and form2.is_valid():
                user = form1.save()
                user.set_password(user.password)
                user.save()
                f2 = form2.save(commit=False)
                f2.user = user
                user2 = f2.save()
                my_student_group = Group.objects.get_or_create(name='STUDENT')
                my_student_group[0].user_set.add(user)
            return HttpResponseRedirect('studentlogin')
        return render(request, 'library/studentsignup.html', context=mydict)

    @login_required(login_url='studentlogin')
    def studentissuedbook(request):
        student = models.Student.objects.filter(user_id=request.user.id)
        issuedbook = models.IssuedBook.objects.filter(id=student[0].id)

        li1 = []

        li2 = []
        for ib in issuedbook:
            books = models.Book.objects.filter(isbn=ib.isbn)
            for book in books:
                t = (request.user, student[0].rolldiv,
                     student[0].branch, book.name, book.author)

                li1.append(t)
            issdate = str(ib.issuedate.day)+'-' + \
                str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
            expdate = str(ib.expirydate.day)+'-' + \
                str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
            # fine calculation
            days = (date.today()-ib.issuedate)
            print(date.today())
            d = days.days
            fine = 0
            if d > 15:
                day = d-15
                fine = day*10
            t = (issdate, expdate, fine)
            li2.append(t)

        return render(request, 'library/studentissuedbook.html', {'li1': li1, 'li2': li2})


class UserList(APIView):

    def get(self, request, format=None):
        user = models.User.objects.all()
        serializer = serializers.UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return models.User.objects.get(pk=pk)
        except models.User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = serializers.UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookList(APIView):

    def get(self, request, format=None):
        book = models.Book.objects.all()
        serializer = serializers.BookSerializer(book, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return models.Book.objects.get(pk=pk)
        except models.Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = serializers.BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = serializers.BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
