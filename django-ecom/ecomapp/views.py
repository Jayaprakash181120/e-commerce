from django.shortcuts import render,redirect
from ecomapp.forms import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def index(request):
    return render(request,'index.html')
def collection(request):
    return render(request,'collection.html')
def contact(request):
    return render(request,'contact.html')

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration Success you can Login Now')
            return redirect('/loginss')
    return render(request,"register.html",{'form':form})


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out Successfully')
    return redirect ("/home")

    

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Sucessfully")
                return redirect("/home")
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect("/login")
        return render(request,"login.html")



