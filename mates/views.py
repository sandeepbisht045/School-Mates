from django.shortcuts import redirect, render
from .models import Mates,User_comments,Users
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random

# Create your views here.
def index(request):
    return render(request,"index.html")

def mates(request):
    welcome=(request.session.get("name"))
    get_data=Mates.objects.all()
    return render(request,"mates.html",{"get_data":get_data,"welcome":welcome})

def add(request):
   if request.method=="POST":
        username=request.session.get("name")
        usermail=request.session.get("email")
        
        if username:
            name=request.POST.get("name")
            about=request.POST.get("about")
            user=Users.objects.get(name=username,email=usermail)
            a=Mates.objects.create(name=name,about=about,added_by=user)
            a.save()
            
            
            # data=Mates(name=name,about=about).save()
            return redirect("/mates")
        else:
            return redirect("/login")
   return render(request,"add.html")


def comment(request):
    comment_fetch=User_comments.objects.all()
    
    if request.method=="POST":
        email=request.session.get("email")
        if email:
            welcome=request.session.get("name")
            comment=request.POST.get("comment")
            user=Users.objects.get(name=welcome,email=email)
            
            a=User_comments.objects.create(comment=comment,user=user)
            a.save()
            return redirect("/comment")
        else:
            return redirect("/login")
        
    return render(request,"comment.html",{"comment_fetch":comment_fetch})

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def signup(request):
    if request.method=="POST":
        usermail=request.POST.get("usermail")
        name=request.POST.get("name")
        password=request.POST.get("password")
        request.session["email"] = usermail      
        Users(name=name,email=usermail,password=password).save()
        request.session["name"] = name     
        return redirect("/mates")
        
    return render(request, "signup.html")

def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
    if request.method=="POST":
        email=request.POST.get("email")
        print(email)
        if Users.objects.filter(email=email).exists():       
            return HttpResponse("")
            
        else:
            o=generateOTP()
            print(o)
            htmlgen = "<p> Your OTP is </p>"  +  " " "<strong>" + str(o)  + "</strong>"
            send_mail('E-mail verification',o,'bishts9796@gmail.com',[email], fail_silently=False, html_message=htmlgen)
            return HttpResponse(o)
 
def login(request):
    return render(request,"login.html")

def login(request):
     request.session.clear() 
     if request.method=="POST":
        usermail=request.POST.get("usermail")
        password=request.POST.get("password")
        filter_data=Users.objects.filter(email=usermail,password=password)
        if filter_data.exists():
            request.session["email"] = usermail
            for i in filter_data:
                request.session["name"] = i.name
            
            return redirect("/mates")
        else:
            return render(request,"login.html",{"error":"Invalid Email or Password"})
     return render(request,"login.html")
 
def logout(request):
    request.session.clear()
    return redirect("/login")
        
    
    
    
    
    
    