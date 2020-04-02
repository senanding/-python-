from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .forms import DIYUserCreationForm
from .models import formalVIP
from django.contrib.auth.decorators import login_required

# Create your views here.

#登录才可以修改查看
@login_required(login_url='myauth:login')
def userCenter(request):#用户中心
    context={'user':request.user}#request.user django模型自带的User
    return render(request,'myauth/userCenter.html',context)

@login_required(login_url='myauth:login')
def editorProfile(request):#编辑个人信息
    if request.method == "POST":
        editorForm = UserChangeForm(request.POST,instance=request.user)#你要修改谁要写清楚
        if editorForm.is_valid():
            editorForm.save()  # 创建并保存,用户信息已经改变了
            return redirect('myauth:userCenter')
    else:
        editorForm = UserChangeForm()
    context = {}
    context["editorForm"] = editorForm
    return render(request, 'myauth/editorProfile.html', context)

@login_required(login_url='myauth:login')
def changePassword(request):# 更改密码
    if request.method=="POST":
        return redirect('myauth:userCenter')
    else:
        return render(request,'myauth/changePassword.html')

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
    if request.method == "POST":
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


