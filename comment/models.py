from django.db import models
from datetime import datetime
# Create your models here.

class Comments(models.Model):
    content=models.TextField(verbose_name='评论内容',default='')
    add_time=models.DateTimeField(verbose_name='发布时间',default=datetime.now)
    author=models.CharField(verbose_name='作者',max_length=255,default='')
    zan=models.IntegerField(verbose_name='点赞数',default=0)
    father=models.IntegerField(verbose_name='父评论ID',default=0)

    class Meta:
        verbose_name='评论'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.content