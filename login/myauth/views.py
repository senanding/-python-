from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import DIYUserCreationForm
from .models import formalVIP

# Create your views here.

def index(request):
    return render(request,'myauth/home.html')

def loginpage(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is None:
            return render(request,'myauth/loginpage.html',{'error':"用户名不存在"})
        else:
            login(request, user)
            return redirect('myauth:index')
    else:
        return render(request,'myauth/loginpage.html')

def mylogout(request):
    logout(request)
    return redirect('myauth:index')

def myregister(request):
    context={}
    registerForm=UserCreationForm()
    context["registerForm"]=registerForm
    return render(request,'myauth/register.html',context)

def myregister(request):
    if request.method=="POST":
        registerForm = DIYUserCreationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            user=authenticate(username=registerForm.cleaned_data["username"],password=registerForm.cleaned_data["password1"])
            user.email = registerForm.cleaned_data['email']
            formalVIP(user=user, nick=registerForm.cleaned_data['昵称'],birthday=registerForm.cleaned_data['生日']).save()
            login(request,user)
            return redirect('myauth:index')
    else:
        registerForm = DIYUserCreationForm(request.POST)
    context = {}
    context["registerForm"]=registerForm
    return render(request,'myauth/register.html',context)

