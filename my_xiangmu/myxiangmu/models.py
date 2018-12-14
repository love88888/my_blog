from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms


# Create your models here.
class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(verbose_name='文章类别', max_length=20)

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    文章标签
    """
    name = models.CharField(verbose_name='文章标签', max_length=20)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




class Blog(models.Model):
    """
    博客
    """
    title = models.CharField(verbose_name='标题', max_length=100)
    content = models.TextField(verbose_name='正文', default='')
    owner = models.ForeignKey(User,verbose_name='作者', on_delete=models.CASCADE,default='')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    click_nums = models.IntegerField(verbose_name='点击量', default=0)
    category = models.ForeignKey(Category, verbose_name='文章类别',on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')

    class Meta:
        verbose_name = '我的博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Comment(models.Model):
    #ForeignKey(User,verbose_name='昵称',on_delete=models.CASCADE)
    username = models.CharField(verbose_name='昵称',max_length=10)
    content = models.TextField(verbose_name='评论内容')
    create_time = models.DateTimeField(verbose_name='评论时间',auto_now_add=True)
    blog = models.ForeignKey(Blog,verbose_name='文章',on_delete=models.CASCADE)


    def __str__(self):
        return self.content[:25]




                # class  look_essay(models.Model):
#     '''
#     浏览文章记录表
#     '''
#     look_title = models.ForeignKey(Blog,verbose_name='浏览文章ID',on_delete=models.CASCADE)
#     look_time = models.DateTimeField(verbose_name='浏览的时间',default=timezone.now)

      # class Meta:
      #     verbose_name = "浏览记录"
      #     verbose_name_plural = verbose_name
#
#     def __str__(self):
#        return self.look_title

# class collect_essay(models.Model):
#       '''
#       收藏文章的表
#       '''
#       collect_title= models.ForeignKey()
      # class Meta:
      #     verbose_name = "浏览记录"
      #     verbose_name_plural = verbose_name