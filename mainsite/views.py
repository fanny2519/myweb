from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here
def homepage(request):   # homepage函数用于获取所有文章
    posts = Post.objects.all()        # 取得所有的数据项
    post_lists = list()
    for count, post in enumerate(posts):    # 通过循环把他们搜集到变量post_list中
        post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
    return HttpResponse(post_lists) # 把变量内容输出到客户端的浏览器页面中
