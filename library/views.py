from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def studentpage(request):
    return render(request, 'studentpage.html')

def adminpage(request):
    return render(request, 'adminpage.html')