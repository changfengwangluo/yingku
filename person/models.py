from django.db import models
from datetime import datetime
# Create your models here.

class Category(models.Model):
    name=models.CharField(verbose_name='类型',max_length=255)

    class Meta:
        verbose_name='人物类型'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Info(models.Model):

    name=models.CharField(verbose_name='姓名',max_length=255)
    ename=models.CharField(verbose_name='英文名',max_length=255,null=True,blank=True)
    jianjie=models.TextField(verbose_name='简介',max_length=255,null=True,blank=True)
    birthday=models.DateField(verbose_name='生日',default=datetime.now,null=True,blank=True)
    fengmian=models.ImageField(verbose_name='封面',upload_to='image/%Y/%m/%d',null=True,blank=True)
    category=models.ManyToManyField(Category,verbose_name='人物类型')
    address=models.CharField(verbose_name='地址',max_length=255,null=True,blank=True)
    xuexing=models.CharField(verbose_name='血型',max_length=255,null=True,blank=True)
    xingzuo=models.CharField(verbose_name='星座',max_length=255,null=True,blank=True)
    zhiye=models.CharField(verbose_name='职业',max_length=255,null=True,blank=True)


    class Meta:
        verbose_name='人物'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name