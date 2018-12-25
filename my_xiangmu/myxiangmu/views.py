import os

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

from myxiangmu.forms import CommentForm
from myxiangmu.models import *
from django.contrib.auth.hashers import make_password, check_password


def index(request):
     # 获取所有的条数
    articles = Blog.objects.all()
    categorys = Category.objects.all()
    essays = Blog.objects.filter(Q(id__gt=5)&Q(id__lt=10))
    return render(request, 'index.html', {'articles':articles,"categorys":categorys,'essays':essays})

# 文章详情页
def article(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    comment = Comment.objects.filter(blog_id=blog_id)
    blog.look_nums += 1
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

# 评论功能
def post(request):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.save()
        return HttpResponse('{"status":"success"}', content_type='application/json')
    else:
        return HttpResponse('{"status":"fail", "msg":"评论错误，请重新评论"}', content_type='application/json')




def category(request,category_id):
    blog = Category.objects.get(id=category_id)
    blogs = Blog.objects.filter(category_id=blog.id)
    return render(request,'category.html',{'blogs':blogs})


#个人中心

def myindex_views(request):
    blog = Blog.objects.filter(owner_id=1)
    per = Perset1.objects.filter(id=1)
    sort1 = Blog.objects.filter(category_id=1,owner_id=1).count()
    sort2 = Blog.objects.filter(category_id=2,owner_id=1).count()
    sort3 = Blog.objects.filter(category_id=3,owner_id=1).count()
    sort4 = Blog.objects.filter(category_id=4,owner_id=1).count()
    sort5 = Blog.objects.filter(category_id=5,owner_id=1).count()
    sort6 = Blog.objects.filter(category_id=6,owner_id=1).count()
    return render(request,'myindex.html',{'per':per,'sort1':sort1,'sort2':sort2,'sort3':sort3,'sort4':sort4,'sort5':sort5,'sort6':sort6,'blog':blog})



def time_views(request):
    articles = Collect_essay.objects.all()
    return render(request,'time.html',{'articles':articles})
#
#
#
#
#
def perSet1_views(request):
    if request.method == 'GET':
        return render(request,'perSet1.html')
    else:
        uname = request.POST.get('uname')
        unichen = request.POST.get('unichen')
        sex = request.POST.get('sex')
        birth = request.POST.get('birth')
        phone = request.POST.get('phone')
        wechart = request.POST.get('wechart')
        Perset1.objects.create(uname=uname,unichen=unichen,sex=sex,birth=birth,phone=phone,wechart=wechart)
        return HttpResponse("<script>alert('保存成功');location.href='/myindex';</script>")



def perSet2_views(request):
    if request.method =='GET':
        return render(request,'perSet2.html')
    else:
        oldpasswd = request.POST.get('oldpasswd')
        password = request.POST.get('password')
        user = User.objects.get(id=2)
        oldpassword = user.password
        if  check_password(oldpasswd,oldpassword):
            passpwd = make_password(oldpasswd)
            user.password=passpwd
            user.save()
            return HttpResponse("<script>alert('修改成功');location.href='/perSet2';</script>")
        else:
            return HttpResponse("<script>alert('密码错误');location.href='/perSet2';</script>")




def sub_views(request):
    if request.method == 'GET':
        return render(request,'submit.html')
    else:
        title = request.POST.get('atitle',None)
        category_id = request.POST.get('fl',None)
        content = request.POST.get('editor1',None)
        if request.FILES:
            # file = request.FILES.get('img')
            # ext = file.name.split('.')[1]
            # filename = title + '.' + ext
            # basedir = os.path.dirname(__file__)
            # upload_path = os.path.join(basedir,'../static/images2/', filename)
            # file.save(upload_path)
            img = request.FILES.get('img')
            f = open(os.path.join('static/images2', title+'.jpg'), 'wb')
            for chunk in img.chunks(chunk_size=1024):
                f.write(chunk)
        Blog.objects.create(title=title,content=content,category_id=category_id,owner_id=1)
        # return HttpResponse('Add Book Success')
        return HttpResponse("<script>alert('保存成功');location.href='/submit';</script>")

#搜索
def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'search_delails.html', {'error_msg': error_msg})

    Sblog = Blog.objects.filter(title__icontains=q)
    return render(request, 'search_delails.html', {'error_msg': error_msg,
                                                 'post_list': Sblog})