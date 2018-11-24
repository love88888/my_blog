from django.shortcuts import render
from django.http import HttpResponse
from myxiangmu.models import Blog, Category, Tag

from django.views import View


# class IndexView(View):
#     """
#     首页
#     """
#     def get(self, request):
#         all_blog = Blog.objects.all().order_by('-id')
#         return render(request, 'index.html', {
#             'all_blog': all_blog,
#         })

def index(request):
    return render(request, 'index.html', context={
                      'title': '我的博客首页',
                      'welcome': '欢迎访问我的博客首页'
                  })



# def index(request):
#     return HttpResponse('欢迎访问我的博客')
