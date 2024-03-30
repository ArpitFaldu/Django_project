from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def logout(request):
    auth.logout(request)
    # messages.info(request,'Logout is successfull')
    return redirect('/')
    


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                messages.info(request,'Sign Up is successfull')
                return redirect('login')
        else:
            messages.info(request,'Password does not match')
            return redirect('signup')
        return redirect('/')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            # messages.info(request,'Login Successful')
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')