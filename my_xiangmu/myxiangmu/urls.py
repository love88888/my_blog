from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/(?P<blog_id>\d+)', views.article, name="blog"),
    url(r'^add_comment', views.post, name='add_comment'),
]


