from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import login as log
from django.contrib.auth import authenticate ,logout
from django.core.paginator import Paginator , EmptyPage
from polls import views
# Create your views here.


#create a poll
def add(request):
 if request.session.has_key('is_logged'): 
    if request.method=='POST':
        a=request.POST['ques']
        b=request.POST['poll1']
        c=request.POST['poll2']
        d=request.POST['poll3']
        e=request.POST['poll4']
        obj=ques(question_text=a,ch1=b,ch2=c,ch3=d,ch4=e,user_name=request.user)
        obj.save()
        return render(request,'choice.html',{'msg':'Poll sucessfully created, View it in My polls !!!'})
    else:
        return render(request,'choice.html')
 else: 
     return redirect('dash')


# List of polls created by user
def detail(request):
 if request.session.has_key('is_logged'): 
    c=ques.objects.filter(user_name=request.user)
    p=Paginator(c,4)
    page_num = request.GET.get('page',1)
    try:
      page_obj = p.get_page(page_num)
    except:
      page_obj = p.get_page(1)
    return render(request,'poll_detail.html',{'res':page_obj})


# delete a polls
def delete(request,id):
    obj = ques.objects.get(id = id)
    obj.delete()
    c =ques.objects.filter(user_name=request.user)
    return render(request,'poll_detail.html',{'res':c})

# edit a poll
def edit(request,id):
  obj=ques.objects.get(id=id)
  c={
    'id':obj.id,
     'ques':obj.question_text,
     'user_name':obj.user_name,
      'poll1':obj.ch1,
      'poll2':obj.ch2,
      'poll3':obj.ch3,
      'poll4':obj.ch4,
     
  }
  return render(request,'update.html',context=c)



#update a poll
def update(request,id):
  obj=ques.objects.get(id=id)
#   obj.user_name=request.POST['user_name']
  obj.ch1=request.POST['poll1']
  obj.ch3=request.POST['poll3']
  obj.ch2=request.POST['poll2']
  obj.ch4=request.POST['poll4']
  obj.question_text=request.POST['ques']
  obj.save()
  c=ques.objects.filter(user_name=request.user)
  return render(request,'poll_detail.html',{'res':c})

def show(request,id):
  obj=ques.objects.get(id=id)
  c={
    'id':obj.id,
     'ques':obj.question_text,
     'user_name':obj.user_name,
      'poll1':obj.ch1,
      'poll2':obj.ch2,
      'poll3':obj.ch3,
      'poll4':obj.ch4,  
  }
  return render(request,'show.html',context=c)



def vote(request, poll1_id):
   poll=ques.objects.get(id=poll1_id)
   if request.method=='POST':
    #  print(request.POST['checkbox'])
     choice=request.POST['checkbox']
     if choice==poll.ch1:
       poll.vote1+=1
     elif choice==poll.ch2:
       poll.vote2+=1
     elif choice==poll.ch3:
       poll.vote3+=1
     elif choice==poll.ch4:
       poll.vote4+=1
     poll.save()
       
     context = {
        'poll' : poll
      }
     return render(request, 'end.html', context)

def result(request,poll1_id):
  poll=ques.objects.get(id=poll1_id)
  context={
    'poll':poll
  }
  return render(request, 'end.html', context)

  