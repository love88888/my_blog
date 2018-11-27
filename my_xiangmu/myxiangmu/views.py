from django.shortcuts import render
from django.http import HttpResponse
from myxiangmu.models import Blog, Category, Tag

from django.views import View
from . import models

# class IndexView(View):
#     """
#     首页
#     """
#     def get(self, request):
#         all_blog = Blog.objects.all().order_by('-id')
#         return render(request, 'index.html', {
#             'all_blog': all_blog,
#         })

# def index(request):
#     return render(request, 'index.html', context={
#                       'title': '游圈',
#                       'welcome': '欢迎访问博客首页'
#                   })



def index(request):
     # 获取所有的条数
    articles = models.Blog.objects.all()
    return render(request, 'index.html', {'articles':articles})
