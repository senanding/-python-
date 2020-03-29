from django.urls import path,include
from . import views

app_name = 'myauth'     #
urlpatterns = [
    path('', views.index, name='index'),  # index=主页
    path('login/',views.loginpage,name="loginpage"),
    path('logout',views.mylogout,name="logout"),# logout=退出登录
    path('registerr/',views.myregister,name="register"),#register=注册
]