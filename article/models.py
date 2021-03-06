from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from film.models import Info as FilmInfo
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

# 影评
class YingPingInfo(models.Model):
    user = models.CharField(verbose_name='作者', max_length=255, default='')
    film = models.CharField(verbose_name='所属电影', max_length=255, default='')
    title = models.CharField(verbose_name='标题', max_length=255, default='')
    content = RichTextUploadingField(verbose_name='内容', default='')
    add_time = models.DateField(verbose_name='发布时间', default=datetime.now)
    zan = models.IntegerField(verbose_name='点赞数', default=0)
    laiyuan = models.CharField(verbose_name='来源', max_length=255, default='')

    class Meta:
        verbose_name = '影评'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 影讯
class YingXunInfo(models.Model):
    title = models.CharField(verbose_name='标题', max_length=255, default='')
    content = RichTextUploadingField(verbose_name='内容', default='')
    add_time = models.DateField(verbose_name='发布时间', default=datetime.now)
    laiyuan = models.CharField(verbose_name='来源', max_length=255, default='')

    class Meta:
        verbose_name = '影讯'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 幕后花絮
class HuaXuInfo(models.Model):
    title = models.CharField(verbose_name='标题', max_length=255,default='')
    content = RichTextUploadingField(verbose_name='内容',default='')
    add_time = models.DateField(verbose_name='发布时间', default=datetime.now)
    film = models.CharField(verbose_name='所属电影', max_length=255,default='')

    class Meta:
        verbose_name = '幕后花絮'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

# 穿帮镜头
class ChuanBang(models.Model):
    content = RichTextUploadingField(verbose_name='内容',default='')
    film = models.CharField(verbose_name='所属电影', max_length=255,default='')

    class Meta:
        verbose_name = '穿帮镜头'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


# 关键词（整个网站的关键词）
class KeyWords(models.Model):
    words = models.CharField(verbose_name='关键词', max_length=255, unique=True,default='')

    class Meta:
        verbose_name = '关键词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.words
