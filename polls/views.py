from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate ,logout
from django.contrib.auth import login as log
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def email(request):
    if request.method == "POST":
        a = request.POST['em']
        b = request.POST['sub']
        c = request.POST['addr']
        send_mail(b,c,settings.EMAIL_HOST_USER,[a],fail_silently=False)
        return render(request,'home.html',{'msg':'Mail send sucessfully'})
    else: 
        return render(request,'home.html')

def sign(request):
    if request.method=='POST':
        a = request.POST['uname']
        b = request.POST['fnm']
        c = request.POST['lnm']
        d = request.POST['em']
        e = request.POST['pasw']
        e1 = request.POST['con']
        if e!=e1:
            return render(request,'sign.html',{'msg':'Password mismatch'})
        if User.objects.filter(username=request.POST['uname']):
            return render(request,'sign.html',{'msg':'Username already taken'})
        else:
           user= User.objects.create_user(username=a,first_name=b,last_name=c,email=d,password=e)
           user.save()
           return redirect('dash')
    else:
        return render(request, 'sign.html')
def login(request):
    if request.method=='POST':
        a = request.POST['uname']
        e = request.POST['pasw']
        obj= User.objects.filter(username=a,password=e)
        f= auth.authenticate(username=a,password=e)
        if f is not None:
            log(request,f)
            request.session['is_logged'] = True
            f = request.user.username
            f1 = request.user.email
            request.session['myname']=f
            request.session['myemail']=f1
            return redirect('dash')
        else:
          return render(request,'login.html',{'msg':'Incorrect username & password'})
    else:
      return render(request,'login.html')
def dash(request):
    if request.session.has_key('myname') and request.session.has_key('myemail'):
          user=request.session['myname']
          email=request.session['myemail']
          return render(request,'dash.html',{'name': user})
    else:
        return render(request,'home.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def change(request):
    if request.method=='POST':
      email=request.POST['email']
      ol_pass=request.POST['old']
      new_pass=request.POST['new']
      con_pass=request.POST['conf']
      obj=User.objects.filter(email=email,password=ol_pass)
      if len(obj)>0:
         if new_pass != con_pass:
           return render(request,'change_pass.html',{'msg':'password mismatch','email':email})
         else:
          obj= User.objects.get(email=email)
          obj.pasw=con_pass
          obj.save()
          return render(request,'change_pass.html',{'email':email,'msg':'congrats! Password change sucessfully'})
      else:
          return render(request,'change_pass.html')
    else:
      return render(request,'change_pass.html')

def change_pass(request):
    if request.session.has_key('myname') and request.session.has_key('myemail'):
          user=request.session['myname']
          email=request.session['myemail']
          return render(request,'change_pass.html',{'email': email})
    else:
        return render(request,'change_pass.html')
