from django.conf.urls import url,include
from django.contrib import admin
# from myxiangmu.views import IndexView



urlpatterns = [
    url(r'^admin/', admin.site.urls),  #后台
    # url(r'^$', IndexView.as_view(), name='index'),
    url(r'', include('myxiangmu.urls')),    #首页的url
    url(r'^users/',include('users.urls',namespace="users")),        #登录注册
]



