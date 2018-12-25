from django.contrib import admin

# Register your models here.
from .models import Category
admin.site.register(Category)

from .models import Tag
admin.site.register(Tag)

from .models import Blog
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title",'owner','click_nums','category','create_time','modify_time','look_nums']
admin.site.register(Blog,BlogAdmin)

from .models import Comment
admin.site.register(Comment)


from .models import Collect_essay
admin.site.register(Collect_essay)

from .models import Perset1
admin.site.register(Perset1)
