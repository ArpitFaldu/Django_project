from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Device
# Create your views here.
def index(request):
    mobile=Device.objects.filter(Type="Mobile")
    laptop=Device.objects.filter(Type="Laptop")
    return render(request,"home.html",{'mobile':mobile,'laptop':laptop})