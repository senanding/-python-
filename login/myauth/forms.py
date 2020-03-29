from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class DIYUserCreationForm(UserCreationForm):
    #自定义注册表单
    nick=forms.CharField(required=True,max_length=50)
    birthday = forms.DateField(required=True)
    class Meta:
        model=User
        fields=('username','password1','password2','email','nick','birthday')