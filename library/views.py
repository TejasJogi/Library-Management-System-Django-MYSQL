from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from . import models, forms
from django.contrib.auth.models import Group

# Create your views here.
def index(request):   
    return render(request, 'index.html')

def studentpage(request):
    return render(request, 'studentpage.html')

def adminpage(request):
    return render(request, 'adminpage.html')

def studentview(request):
    books = models.Book.objects.all()
    return render(request,'studentview.html',{'books': books})


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
    return render(request, 'adminsignup.html', {'form': form})


def adminlogin(request):
    return render(request, 'adminlogin.html')


def adminauth(user):
    return user.groups.filter(name='ADMIN').exists()


def admindash(request):
    return render(request, 'admindash.html')


def addbook(request):
    form = forms.BookForm()
    if request.method == 'POST':
        form = forms.BookForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'bookadded.html')
    return render(request, 'addbook.html', {'form': form})


def viewbook(request):
    books = models.Book.objects.all()
    return render(request, 'viewbook.html', {'books': books})


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
    return render(request, 'addbook.html', locals())




def bookdelete(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    obj = get_object_or_404(models.Book, id=pk)
    obj.delete()
    # return redirect('index')
    return redirect('admindash.html')
