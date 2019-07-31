from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # url('^login/$',views.login,name="login"),
    url(r'^register/$',views.Register.as_view(),name="register"),
]