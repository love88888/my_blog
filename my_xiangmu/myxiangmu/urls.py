<<<<<<< 8d74020a5db3dbc527b3f52e59962c14e59879eb
from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^blog/(?P<blog_id>\d+)/$',views.article,name="blog"),      #博客详情页
    url(r'^category/(?P<category_id>\d+)$',views.category, name="category"), #分类
    # url(r"^article_add/", views.article_add, name="article_add")  #评论
]
=======
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]


>>>>>>> 第er次
