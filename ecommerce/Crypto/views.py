from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def registerview(request):
    return render(request,"register.html")
def loginview(request):
    return render(request,'login.html')
def aboutview(request):
    return render(request,'about.html')
def helpview(request):
    return render(request,'help.html')
def teamview(request):
    return render(request,'team.html')
