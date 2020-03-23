from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'myauth/home.html')

def login(request):
    return render(request,'myauth/login.html')

'''from django.shortcuts import render,redirect
def mylogin(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is None:
            return render(request,'myauth/login.html',{'error':"用户名不存在"})
        else:
            login(request,user)
            return redirect('myauth:index')

    else:
        return render(request,'myauth/login.html'''