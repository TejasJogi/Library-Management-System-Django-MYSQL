from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    return render(request, 'index.html')

def studentpage(request):
    return render(request, 'studentpage.html')

def adminpage(request):
    return render(request, 'adminpage.html')

def studentview(request):
    books=models.Book.objects.all()
    return render(request,'studentview.html')