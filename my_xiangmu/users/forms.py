from django import forms
from .models import *


class UserRegister(forms.Form):
    username = forms.CharField(label="用户名", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="确认密码", max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserLogin(forms.Form):
    username = forms.CharField(label="用户名", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))