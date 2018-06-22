from django.db import models
from person.models import Info as PersonInfo
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name=models.CharField(verbose_name='类型',max_length=255,unique=True)

    class Meta:
        verbose_name='电影类型'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


class Info(models.Model):
    name=models.CharField(verbose_name='电影名',max_length=255,unique=True)
    ename=models.CharField(verbose_name='英文名',max_length=255,null=True,blank=True)
    yiming=models.CharField(verbose_name='译名',max_length=255,null=True,blank=True)
    jianjie=models.TextField(verbose_name='汉语简介',null=True,blank=True)#短
    juqing=models.TextField(verbose_name='汉语剧情',null=True,blank=True)#长
    ejianjie = models.TextField(verbose_name='英语简介',null=True,blank=True)  # 短
    ejuqing = models.TextField(verbose_name='英语剧情',null=True,blank=True)  # 长
    jibie = models.TextField(verbose_name='电影级别',null=True,blank=True)
    daoyan=models.CharField(verbose_name='导演',max_length=255,null=True,blank=True)
    bianju=models.CharField(verbose_name='编剧',max_length=255,null=True,blank=True)
    category=models.ManyToManyField(Category,verbose_name='类型',null=True,blank=True)
    yanyuan=models.ManyToManyField(PersonInfo,verbose_name='演员',null=True,blank=True)
    chupingongsi=models.CharField(verbose_name='出品公司',max_length=255,null=True,blank=True)
    zhipiangongsi=models.CharField(verbose_name='制片公司',max_length=255,null=True,blank=True)
    shichang=models.CharField(verbose_name='时长',max_length=255,null=True,blank=True)
    zhipiandiqu=models.CharField(verbose_name='制片地区',max_length=255,null=True,blank=True)
    chengben=models.CharField(verbose_name='制片成本',max_length=255,null=True,blank=True)
    year=models.CharField(verbose_name='年代',max_length=255,null=True,blank=True)
    paishedi=models.CharField(verbose_name='拍摄地点',max_length=255,null=True,blank=True)
    duibai=models.CharField(verbose_name='对白语言',max_length=255,null=True,blank=True)
    paisheriqi=models.CharField(verbose_name='拍摄日期',max_length=255,null=True,blank=True)
    secai=models.CharField(verbose_name='色彩',max_length=255,null=True,blank=True)
    imdb=models.CharField(verbose_name='IMDB编码',max_length=255,null=True,blank=True)
    add_time=models.DateField(verbose_name='收录时间',default=datetime.now,null=True,blank=True)
    misuc=models.CharField(verbose_name='电影原声',max_length=255,null=True,blank=True)
    db_fen=models.IntegerField(verbose_name='豆瓣评分',null=True,blank=True)
    imdb_fen=models.IntegerField(verbose_name='IMDB评分',null=True,blank=True)
    youku=models.TextField(verbose_name='优酷地址',null=True,blank=True)
    bilibili=models.TextField(verbose_name='bilibili地址',null=True,blank=True)
    aiqiyi=models.TextField(verbose_name='爱奇艺',null=True,blank=True)

    class Meta:
        verbose_name='电影'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(verbose_name='角色名', max_length=255)
    film=models.ForeignKey(Info,verbose_name='所属电影',on_delete=models.DO_NOTHING)
    yanyuan=models.ForeignKey(PersonInfo,verbose_name='扮演者',on_delete=models.DO_NOTHING)
    desc=models.TextField(verbose_name='角色描述',null=True,blank=True)
    fengmian=models.ImageField(verbose_name='角色封面',upload_to='image/%Y/%m/%d',null=True,blank=True)

    class Meta:
        verbose_name='角色'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class HonorCategory(models.Model):
    name= models.CharField(verbose_name='名称', max_length=255)

    class Meta:
        verbose_name='电影奖名称'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


class Honor(models.Model):
    RESULT=(
        ('hj','获奖'),
        ('tm','提名'),
    )
    category=models.ForeignKey(HonorCategory,verbose_name='所属奖',on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name='奖项', max_length=255)
    person=models.ManyToManyField(PersonInfo,verbose_name='获奖者',null=True,blank=True)
    film=models.ForeignKey(Info,verbose_name='获奖电影',on_delete=models.DO_NOTHING,null=True,blank=True)
    result=models.CharField(verbose_name='结果',choices=RESULT,max_length=255)

    class Meta:
        verbose_name = '电影奖'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Show(models.Model):
    time=models.DateField(verbose_name='上映时间',max_length=255)
    address=models.CharField(verbose_name='国家/地区',max_length=255)
    film=models.ForeignKey(Info,verbose_name='所属电影',on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = '上映时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.time)


class PiaoFang(models.Model):
    num = models.IntegerField(verbose_name='收入')
    address = models.CharField(verbose_name='国家/地区',max_length=255)
    film = models.ForeignKey(Info,verbose_name='所属电影',on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = '票房'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.num)

class ZhaiYao(models.Model):
    film = models.ForeignKey(Info, verbose_name='所属电影', on_delete=models.DO_NOTHING)
    content=models.TextField(verbose_name='摘要内容')

    class Meta:
        verbose_name = '摘要'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.film.name

class Shanging(models.Model):
    shijian=models.CharField(verbose_name='时间',max_length=255)
    film = models.ForeignKey(Info, verbose_name='所属电影', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = '上映时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.shijian
