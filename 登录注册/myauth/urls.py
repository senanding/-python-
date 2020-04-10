from django.urls import path,include
from . import views

app_name = 'myauth'     #
urlpatterns = [
    path('', views.index, name='index'),  # index=主页
    path('login/',views.loginpage,name="loginpage"),
    path('logout',views.mylogout,name="logout"),# logout=退出登录
    path('register/',views.myregister,name="register"),#register=注册
    path('userCenter/',views.userCenter,name="userCenter"),#个人中心
    path('userCenter/editProfile',views.editorProfile,name="editorProfile"),#编辑个人信息
    path('userCenter/changePassword',views.changePassword,name="changePassword"),#修改密码
    path('indexpage/',views.indexpage,name="indexpage"),
    path('bind/', views.bind, name="bind"),
]