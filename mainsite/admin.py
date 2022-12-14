from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')  # 显示张贴的日期和时间


admin.site.register(Post, PostAdmin)
