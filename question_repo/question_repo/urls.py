
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('apps.accounts.urls',namespace="accounts")),
    url(r'^', include('apps.repo.urls', namespace="repo")),
    url(r'^usercenter/',include('apps.usercenter.urls',namespace="usercenter")),
    url(r'^apis/',include('apps.apis.urls',namespace="apis")),
    url(r'^$',views.index),

    url(r'^logtest/$',views.logtest,name="logtest"),

    # meida 处理
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # ckeditor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # 测试paginator
    url(r'^paginator/$',views.test)
]
