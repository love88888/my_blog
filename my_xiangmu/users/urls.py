from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    #用户名
    url(r'^login/$',views.login, {'template_name': 'users/login.html'},
        name='login'),

    # 注销页面
    url(r'^logout/$', views.logout_view, name='logout'),

    # 注册页面。
    url(r'^register/$', views.register, name='register'),
]

