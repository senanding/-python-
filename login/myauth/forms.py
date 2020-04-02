from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class DIYUserCreationForm(UserCreationForm):
    # 自定义注册表单
    nick = forms.CharField(required=True, max_length=50)
    birthday = forms.DateField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'nick', 'birthday')

#出错，未能解决
def __init__(self, *args, **kwargs):  # 初始化构造函数
    super().__init__(*args, **kwargs)  # 上一级的初始化函数
    self.fields['username'].error_messages = {'unique': '用户名已存在', 'invalid': '格式不对'}  # 用户名相同产生的错误