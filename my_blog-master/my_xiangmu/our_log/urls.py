from django.conf.urls import url,include
from django.contrib import admin
# from myxiangmu.views import IndexView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', IndexView.as_view(), name='index'),  #首页的url
    url(r'', include('myxiangmu.urls')),
]



