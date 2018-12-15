from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^blog/(?P<blog_id>\d+)/$',views.article,name="blog"),      #博客详情页
    url(r'^category/(?P<category_id>\d+)$',views.category, name="category"), #分类
    # url(r"^article_add/", views.article_add, name="article_add")  #评论
]
