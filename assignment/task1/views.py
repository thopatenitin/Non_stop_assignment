from django.shortcuts import render,redirect
from .models import post
from .forms import post_form,post_update_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import date
import os
from django.conf import settings
# Create your views here.

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"Invalid Username")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"Username or Password is invalid")
    context={}
    return render(request,'task1/login_register.html',context) 


def logoutUser(request):
        logout(request)
        return redirect("home")

def view_post(request,id):
    all=post.objects.filter(pk=id)
    imagePath =[img.image for img in all][0]
    print(imagePath)
    imageSource=os.path.join(settings.MEDIA_ROOT,str(imagePath))
    context={
        "all":all,
        "imageSource":imageSource
    }
    # print(all_posts.content)
    return render(request,'task1/view_post.html',context)
    
@login_required(login_url="loginUser")
def postsInsert(request):
    form=post_form()

    context={
        "form":form
    }
    if request.method =="POST":
        form=post_form(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            UserPost=form.save(commit=False)
            if request.POST.get("publish")=="True":
                UserPost.published=True
                UserPost.published_date=date.today()
            else:
                UserPost.published=False
                UserPost.published_date=None    

            UserPost.author=request.user
            UserPost.save()
            
            return redirect("home")
        else:
            print("Form is Invalid")
            print(form.errors)
            return render(request, 'task1/insert_post.html', {'form': form, 'errors': form.errors})
        
    return render(request,"task1/insert_post.html",context)

@login_required(login_url="loginUser")
def update_post(request,id):
    oldPost=post.objects.get(pk=id)
    form=post_update_form(instance=oldPost)
    context={"form":form}
    if request.method=="POST":
        form =post_update_form(request.POST,instance=oldPost)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return HttpResponse("Update failed")
    return render(request,"task1/update_post.html",context)

@login_required(login_url="loginUser")
def delete_post(request,id):
    existingPost=post.objects.get(pk=id)
    if request.method=='POST':
        existingPost.delete()
        return redirect("home")
    return render(request,'task1/delete_post.html',{"obj":existingPost})


def home(request):
    q=request.GET.get("q") if request.GET.get("q")!=None else ''
    if q=="published":
        post_temp=post.objects.filter(Q(published=True)& Q(author=request.user))
    elif q=="drafts":
        post_temp=post.objects.filter(Q(published=False)& Q(author=request.user))
    else:
        post_temp=post.objects.filter(published=True)
    
    context={
        "posts":post_temp,
        "count":post_temp.count()
    }
    print(context)
    return render(request,"task1/home.html",context)


def publish_post(request,id):
    usersPost=post.objects.get(pk=id)
    if request.method=="POST":
        usersPost.published=True
        usersPost.published_date=date.today()
        usersPost.save()
        return redirect("home")
    return render(request,'task1/publish_post.html',{})
