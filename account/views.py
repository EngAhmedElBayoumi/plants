from django.shortcuts import render
#import login and logout
from django.contrib.auth import login,logout
# import authenticate
from django.contrib.auth import authenticate
# import redirect
from django.shortcuts import redirect
# import user
from django.contrib.auth.models import User
# import messages
from django.contrib import messages
# Create your views here.

def log_in(request):
    #login function 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home:home')
        else:
            messages.error(request,'اسم المستخدم او كلمه المرور غير صحيحه')
    return render(request,'login.html')

def sign_in(request):
    #signin function
    if request.method =="POST":
      username = request.POST['username']
      password = request.POST['password']
      password2 = request.POST['password2']
      email = request.POST['email']
      
      if password== password2:
        #check is user is aready exist
        if User.objects.filter(username=username).exists():
            messages.error(request,'اسم المستخدم موجود مسبقا')
            return redirect('account:signin_ar')
        else:
            myuser= User.objects.create_user(username,email,password)
            myuser.save()
            return redirect('account:login_ar')
      else:
           messages.error(request,'كلمه المرور غير متطابقه')
    return render(request,'register-ar.html')

def log_out(request):
    logout(request)
    return redirect('account:login_ar')


#ar
def log_in_ar(request):
    #login function 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home:home_ar')
        else:
            messages.error(request,'اسم المستخدم او كلمه المرور غير صحيحه')
    return render(request,'login-ar.html')

def sign_in_ar(request):
    #signin function
    if request.method =="POST":
      username = request.POST['username']
      password = request.POST['password']
      password2 = request.POST['password2']
      email = request.POST['email']
      
      if password== password2:
        #check is user is aready exist
        if User.objects.filter(username=username).exists():
            messages.error(request,'اسم المستخدم موجود مسبقا')
            return redirect('account:signin_ar')
        else:
            myuser= User.objects.create_user(username,email,password)
            myuser.save()
            return redirect('account:login_ar')
      else:
           messages.error(request,'كلمه المرور غير متطابقه')
    return render(request,'register-ar.html')

def log_out_ar(request):
    logout(request)
    return redirect('account:login_ar')