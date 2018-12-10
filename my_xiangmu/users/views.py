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

    logout(request)
    return HttpResponseRedirect(reverse('templates:index'))


def register(request):
    """注册一个新用户"""
    if request.method != 'POST':
        # 显示空白注册表
        form = UserCreationForm()
    else:
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





