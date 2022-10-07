from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):     // 创建一个post类
  title = models.CharField(max_length=200)
  slug = models.CharField(max_length=200)   // 文章的网址
  body = models.TextField()     // 文章的内容
  pub_date = models.DateTimeField(default=timezone.now)    // 文本发表的时间
  
  class Meta:
    ordering = ('-pub_date',)   // 指定文章显示的顺序是以pub_date为依据
    
   def __str__(self):
    return self.title    // 提供此类产生的数据项--一个以文章标题作为显示的内容
