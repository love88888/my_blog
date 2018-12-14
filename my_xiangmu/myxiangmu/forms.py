<<<<<<< HEAD
from django import forms
from myxiangmu.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'content','blog']
=======
# from django import  forms
# from myxiangmu.models import Comment
#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['name', 'content', 'blog']

>>>>>>> d9ee139f14358d29d802e377ca5c730be9f557ac
