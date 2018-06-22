from django.db import models

# Create your models here.


class LunBo(models.Model):
    img=models.ImageField(verbose_name='图片',upload_to='image/%Y/%m/%d')
    title=models.CharField(verbose_name='标题',max_length=255,null=True,blank=True)
    desc=models.CharField(verbose_name='描述',max_length=255,null=True,blank=True)
    url=models.CharField(verbose_name='链接',max_length=255)

    class Meta:
        verbose_name='轮播图'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title

class Link(models.Model):

    name = models.CharField(verbose_name='网站名', max_length=255)
    url = models.CharField(verbose_name='链接', max_length=255)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
