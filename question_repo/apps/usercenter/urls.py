from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    # 修改资料
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    # 修改密码
    url(r'^change_passwd/$', views.ChangePasswdView.as_view(), name='change_passwd'),
    # 查看我的回答
    url(r'^answer/$', views.AnswerView.as_view(), name='answer'),
    # 用户权限控制
    url(r'^approval/$', views.ApprovalView.as_view(), name='approval'),
]