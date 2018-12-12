<<<<<<< 8d74020a5db3dbc527b3f52e59962c14e59879eb



=======
from django.forms import forms, models
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, request
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from users.forms import UserRegister, UserLogin
from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User
import hashlib

# Create your views here.

def index_views(request):
    return render(request,'index.html')
# Create your views here.
#创建加密函数
def hash_lib(content):
    hash = hashlib.md5()
    hash.update(content.encode())
    result = hash.hexdigest()
    return  result
#注册
def register(request):
    if request.method == "GET":
        return render(request,'users/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        namefilter = User.objects.filter(username=username)
        if len(namefilter) > 0:
            return render(request,'users/register.html',{'error':'用户名已存在'})
        elif username == '' or len(username.split(' ')) > 1:
            return render(request,'users/register.html',{'error':'用户名不能为空或含有空格'})
        elif len(username) < 2:
            return render(request,'users/register.html',{'error':'用户名过短'})

        password = request.POST['upwd']
        password1 = request.POST['upwds']
        if password1 != password:
            return render(request, 'users/register.html', {'error':'两次输入的密码不一致！'})
        elif len(password) < 8:
            return render(request,'users/register.html',{'error':'密码长度不足'})

        password = hash_lib(password1)
        user = User.objects.create(username=username, password=password)
        user.save()
        return render(request, 'users/success.html', {'username': username, 'operation': '注册'})




#登录
def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid(): #获取表单信息
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password = hash_lib(password)
            namefilter = User.objects.filter(username=username,password=password)
            if len(namefilter) > 0:
                return render(request,'users/success.html',{'username':username,'operation':'登录'})
            else:
                return render(request, 'users/login.html', {'error':'该用户名不存在！'})
    else:
        form =UserLogin()
        return render(request,'users/login.html', {'form':form})































# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         message = "所有字段都必须填写！"
#         if username and password:
#             username = username.strip()
#             try:
#                 user = models.User.objects.get(name=username)
#                 if user.password == password:
#                     return redirect('/index/')
#                 else:
#                     message = "密码不正确！"
#             except:
#                 message = "用户名不存在！"
#         return render(request, 'users/login.html', {"message": message})
#     return render(request, 'users/login.html')
#
# def register(request):
#     if request.method == "POST":
#         username = request.POWT.get('username')
#
#
#
#
#
# def register(request):
#     if request.method == "POST":
#         from my_blog.my_xiangmu.users.forms import RegisterForm
#         register_form = RegisterForm(request.POST)
#         message = "请检查填写的内容！"
#         if register_form.is_valid():
#             username = register_form.cleaned_data['username']
#             password = register_form.cleaned_data['password']
#             password1 = register_form.cleaned_data['password1']
#             if password != password1:
#                 message = "两次输入的密码不同！"
#                 return render(request, 'login/register.html', locals())
#             else:
#                 same_name_user = models.User.objects.filter(name=username)
#                 if same_name_user:
#                     message = '用户已经存在，请重新选择用户名！'
#                     return render(request, '/users/register.html', locals())
#
#                 new_user = models.User.objects.create()
#                 new_user.name = username
#                 new_user.password = password1
#                 return redirect('/users/login.html')
#     register_form = RegisterForm()
#     return render(request, '/users/register.html', locals())
>>>>>>> 第er次

