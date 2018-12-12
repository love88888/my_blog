from django.contrib import admin

<<<<<<< 8d74020a5db3dbc527b3f52e59962c14e59879eb
=======
# Register your models here.
>>>>>>> 第er次
from .models import Category
admin.site.register(Category)

from .models import Tag
admin.site.register(Tag)

from .models import Blog
class BlogAdmin(admin.ModelAdmin):
<<<<<<< 8d74020a5db3dbc527b3f52e59962c14e59879eb
    list_display = ["title",'owner','click_nums','category','create_time','modify_time','look_nums']
admin.site.register(Blog,BlogAdmin)

from .models import Comment
admin.site.register(Comment)


from .models import Collect_essay
admin.site.register(Collect_essay)
=======
    list_display = ["title",'owner','click_nums','category','create_time','modify_time']
admin.site.register(Blog,BlogAdmin)
>>>>>>> 第er次
