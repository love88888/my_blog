<<<<<<< HEAD
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
=======
from django.contrib import auth
from django.forms import Form
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


# def login(request):
#     return  render(request, "users/login.html")
#
def logout_view(request):
>>>>>>> d9ee139f14358d29d802e377ca5c730be9f557ac

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
<<<<<<< HEAD
        form =UserLogin()
        return render(request,'users/login.html', {'form':form})
=======
        #
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 登录用户，然后重定向到主页。
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('templates:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('login:home'))
    else:
        return render(request, 'login.html', {
            'username': username,
            'password': password,
        })




>>>>>>> d9ee139f14358d29d802e377ca5c730be9f557ac

