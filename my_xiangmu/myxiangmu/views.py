from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from myxiangmu.models import Blog, Category, Tag,Comment
from myxiangmu.forms import CommentForm

=======

# from myxiangmu.forms import CommentForm
from myxiangmu.models import Blog, Category, Tag,Comment
>>>>>>> d9ee139f14358d29d802e377ca5c730be9f557ac

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
<<<<<<< HEAD
    articles = models.Blog.objects.all()
    return render(request, 'index.html', {'articles':articles})

def article(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    comment = Comment.objects.filter(blog_id=blog_id)
    blog.click_nums += 1
    blog.save()
    comment_nums =comment.count()
    has_prev = False
    has_next = False
    id_prev = id_next = int(blog_id)
    blog_id_max = Blog.objects.all().order_by('-id').first()
    id_max = blog_id_max.id
    while not has_prev and id_prev >= 1:
        blog_prev = Blog.objects.filter(id = id_prev - 1).first()
        if not blog_prev:
            id_prev -= 1
        else:
            has_prev = True
    while not has_next and id_next <= id_max:
        blog_next = Blog.objects.filter(id = id_next + 1).first()
        if not blog_next:
            id_next += 1
        else:
            has_next = True;
    return render(request, 'infos.html', {
        'blog': blog,
        'comment': comment,
        'comment_nums':comment_nums,
        'blog_prev': blog_prev,
        'blog_next':blog_next,
        'has_prev': has_prev,
        'has_next': has_next,
                  })

def post(request):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.save()
        return HttpResponse('{"status":"success"}', content_type='application/json')
    else:
        return HttpResponse('{"status":"fail", "msg":"评论错误，请重新评论"}', content_type='application/json')








=======
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



def article_add(request):
    if request.method=="POST":
        #添加进数据库
        username= request.POST.get("username")
        created_time = request.POST.get("created_time")
        blog_id = request.POST.get("blog_id")
        content =  request.POST.get("content")
        Comment.objects.create(username=username,created_time=created_time,content=content,blog_id=blog_id)
        #查询博客的详情属性
        blog = Blog.objects.get(id=blog_id)
        comment = Comment.objects.filter(blog_id=blog_id)
        return render(request, 'article_content.html', {'blog': blog,'comment':comment})
>>>>>>> d9ee139f14358d29d802e377ca5c730be9f557ac

