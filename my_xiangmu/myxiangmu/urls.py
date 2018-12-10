from django.conf.urls import url
from . import views
from myxiangmu.views import AddCommentView


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/(?P<blog_id>\d+)/$',views.article,name="blog"),      #博客详情页
    url(r'^category/(?P<category_id>\d+)$',views.category, name="category"), #分类
    url(r'^add_comment/$',AddCommentView.as_view(), name='add_comment'),  #评论
]
