from django.shortcuts import render
from django.http import HttpResponse

# from myxiangmu.forms import CommentForm
from myxiangmu.models import Blog, Category, Tag,Comment

from django.views import View
from . import models


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




