from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    #用户名
<<<<<<< HEAD
    url(r'^login/$',views.login,name='login'),

    # 注销页面
    #url(r'^logout/$', views.logout_view, name='logout'),
    #
    # 注册页面。
    url(r'^register/$', views.register,name='register'),
]
=======
    url(r'^login/$',views.login, {'template_name': 'users/login.html'},
        name='login'),

    # 注销页面
    url(r'^logout/$', views.logout_view, name='logout'),

    # 注册页面。
    url(r'^register/$', views.register, name='register'),
]

>>>>>>> d9ee139f14358d29d802e377ca5c730be9f557ac
