from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/(?P<blog_id>\d+)', views.article, name="blog"),      #博客详情页
    url(r'^category/(?P<category_id>\d+)$',views.category, name="category"), #分类
    url(r'^add_comment', views.post, name='add_comment'),  #评论
    url(r'^myindex/$',views.myindex_views,name="myindex"),
    url(r'^perSet1/$', views.perSet1_views,name="perSet1"),
    url(r'^perSet2/$', views.perSet2_views,name="perSet2"),
    url(r'^submit/', views.sub_views,name="submit"),
    url(r'^time/', views.time_views,name="time"),
    url(r'^search/',views.search,name='search'),
]
