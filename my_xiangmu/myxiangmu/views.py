from django.shortcuts import render
from django.http import HttpResponse

from myxiangmu.forms import CommentForm
from myxiangmu.models import Blog, Category, Tag,Comment

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
    articles = Blog.objects.all()
    categorys = Category.objects.all()
    return render(request, 'index.html', {'articles':articles,"categorys":categorys})


def article(request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        comment = Comment.objects.filter(blog_id=blog_id)
        return render(request, 'article_content.html', {'blog': blog,'comment':comment})

def category(request,category_id):
    blog = Category.objects.get(id=category_id)
    blogs = Blog.objects.filter(category_id=blog.id)
    return render(request,'category.html',{'blogs':blogs})



class AddCommentView(View):
    def post(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail"}', content_type='application/json')

