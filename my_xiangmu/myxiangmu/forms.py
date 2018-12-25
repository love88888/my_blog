from django import forms
from myxiangmu.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'content','blog']
