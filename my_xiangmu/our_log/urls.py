from django.conf.urls import url,include
from django.contrib import admin
# from myxiangmu.views import IndexView



urlpatterns = [
    url(r'^admin/', admin.site.urls),  #后台
    # url(r'^$', IndexView.as_view(), name='index'),
<<<<<<< 8d74020a5db3dbc527b3f52e59962c14e59879eb
    url(r'', include('myxiangmu.urls',namespace='myxiangmu')),    #首页的url
=======
    url(r'', include('myxiangmu.urls')),    #首页的url
>>>>>>> 第er次
    url(r'^users/',include('users.urls',namespace="users")),        #登录注册
]



