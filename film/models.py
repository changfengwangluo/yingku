from django.db import models
from person.models import Info as PersonInfo
from datetime import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='类型', max_length=255, unique=True)

    class Meta:
        verbose_name = '电影类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Info(models.Model):
    name = models.CharField(verbose_name='电影名', max_length=255, unique=True, default='')
    ename = models.CharField(verbose_name='英文名', max_length=255, default='')
    jianjie = models.TextField(verbose_name='简介', default='')
    juqing = models.TextField(verbose_name='剧情', default='')
    jibie = models.TextField(verbose_name='电影级别', default='')
    category = models.CharField(verbose_name='电影类型', max_length=255, default='')
    guojia = models.CharField(verbose_name='国家/地区', max_length=255, default='')
    chupingongsi = models.TextField(verbose_name='出品公司', max_length=255, default='')
    zhipiangongsi = models.TextField(verbose_name='制片公司', max_length=255, default='')
    shichang = models.CharField(verbose_name='时长', max_length=255, default='')
    zhipiandiqu = models.CharField(verbose_name='制片地区', max_length=255, default='')
    chengben = models.CharField(verbose_name='制片成本', max_length=255, default='')
    year = models.CharField(verbose_name='年代', max_length=255, default='')

    duibai = models.CharField(verbose_name='对白语言', max_length=255, default='')
    paisheriqi = models.CharField(verbose_name='拍摄日期', max_length=255, default='')
    secai = models.CharField(verbose_name='色彩', max_length=255, default='')
    imdb = models.CharField(verbose_name='IMDB编码', max_length=255, default='')
    add_time = models.DateField(verbose_name='收录时间', default=datetime.now)
    misuc = models.CharField(verbose_name='电影原声', max_length=255, default='')
    db_fen = models.FloatField(verbose_name='豆瓣评分', default=0)
    imdb_fen = models.FloatField(verbose_name='IMDB评分', default=0)
    youku = models.TextField(verbose_name='优酷地址', default='')
    bilibili = models.TextField(verbose_name='bilibili地址', default='')
    aiqiyi = models.TextField(verbose_name='爱奇艺', default='')

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#角色
class Role(models.Model):
    name = models.CharField(verbose_name='角色名', max_length=255, default='')
    film = models.CharField(verbose_name='所属电影', max_length=255, default='')
    yanyuan = models.CharField(verbose_name='演员', max_length=255, default='')
    desc = models.TextField(verbose_name='角色描述', default='')
    fengmian = models.ImageField(verbose_name='角色封面', upload_to='image/%Y/%m/%d', default='')

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#电影奖名称
class HonorCategory(models.Model):
    name = models.CharField(verbose_name='名称', max_length=255, default='')

    class Meta:
        verbose_name = '电影奖名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#电影奖
class Honor(models.Model):
    RESULT = (
        ('hj', '获奖'),
        ('tm', '提名'),
    )
    category = models.CharField(verbose_name='所属奖', max_length=255, default='')
    name = models.CharField(verbose_name='奖项', max_length=255, default='')
    person = models.CharField(verbose_name='获奖者', max_length=255, default='')  # ?
    film = models.CharField(verbose_name='所属电影', max_length=255, default='')
    result = models.CharField(verbose_name='结果', choices=RESULT, max_length=255, default='tm')

    class Meta:
        verbose_name = '电影奖'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#票房
class PiaoFang(models.Model):
    num = models.IntegerField(verbose_name='收入', default='')
    address = models.CharField(verbose_name='国家/地区', max_length=255, default='')
    film = models.CharField(verbose_name='所属电影', max_length=255, default='')

    class Meta:
        verbose_name = '票房'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.num)


# 电影介绍摘要
class ZhaiYao(models.Model):
    film = models.CharField(verbose_name='所属电影', max_length=255, default='')
    content = models.TextField(verbose_name='摘要内容', default='')

    class Meta:
        verbose_name = '摘要'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.film.name


# 上映时间
class ShangYing(models.Model):
    shijian = models.CharField(verbose_name='时间', max_length=255, default='')
    guojia = models.CharField(verbose_name='国家', max_length=255, default='')
    chengshi = models.CharField(verbose_name='城市', max_length=255, default='')
    film = models.CharField(verbose_name='所属电影', max_length=255, default='')

    class Meta:
        verbose_name = '上映时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.shijian


# 国家/地区
class GuoJia(models.Model):
    film = models.CharField(verbose_name='所属电影', max_length=255, default='')
    name = models.CharField(verbose_name='国家/地区(中文)', max_length=255, default='')
    ename = models.CharField(verbose_name='国家/地区(英文)', max_length=255, default='')

    class Meta:
        verbose_name = '国家/地区'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 译名/别名
class YiMing(models.Model):
    film = models.CharField(verbose_name='所属电影', max_length=255, default='')
    guojia = models.CharField(verbose_name='国家/地区', max_length=255, default='')
    name = models.CharField(verbose_name='译名/别名', max_length=255, default='')

    class Meta:
        verbose_name = '译名/别名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 演员+职员
class YanZhiYuan(models.Model):
    # 演职人员身份
    CG = (
        ('yy', '主演'),  # Cast (in credits order) verified as complete 主要演员|Rest of cast listed alphabetically其他演员
        ('dy', '导演'),  # Directed
        ('bj', '编剧'),  # Writing Credits
        ('zp', '制片人'),  # Produced
        ('ms', '音乐'),  # Music
        ('sy', '摄影'),  # Cinematography
        ('jj', '剪辑'),  # Film Editing
        ('tx', '角色挑选'),  # Casting By
        ('zp', '制片设计'),  # Production Design
        ('hz', '化妆'),  # Makeup Department
        ('sc', '生产管理'),  # Production Management
        ('zl', '助理导演'),  # Second Unit Director or Assistant Director
        ('ad', '美术'),  # Art Department
        ('yx', '音效'),  # Sound Department
        ('tx', '特效'),  # Special Effects
        ('sj', '视觉'),  # Visual Effects
        ('tj', '特技'),  # Stunts
        ('dj', '道具场工'),  # Electrical Department
        ('dh', '动画'),  # Animation Department
        ('dp', '底片冲印'),  # Casting Department
        ('fz', '服装管理'),  # Costume and Wardrobe Department
        ('zb', '助理编辑'),  # Editorial Department
        ('cj', '场景管理'),  # Location Management
        ('md', '音乐部门'),  # Music Department
        ('ys', '底片运送'),  # Transportation Department
        ('qt', '其他职员'),  # Other crew
    )
    film = models.CharField(verbose_name='所属电影', max_length=255, default='')
    name = models.CharField(verbose_name='姓名', max_length=255, default='')
    ename = models.CharField(verbose_name='英文名', max_length=255, default='')
    category = models.CharField(verbose_name='身份', choices=CG, max_length=255, default='')  # 人员类型
    image = models.CharField(verbose_name='头像', max_length=255, default='')
    beizhu = models.CharField(verbose_name='备注', max_length=255, default='')

    class Meta:
        verbose_name = '演职人员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 拍摄地
class PaiSheDi(models.Model):
    film = models.CharField(verbose_name='所属电影', max_length=255, default='')
    address = models.CharField(verbose_name='国家/地区', max_length=255, default='')
    changjing = models.CharField(verbose_name='电影场景', max_length=255, default='')

    class Meta:
        verbose_name = '拍摄地'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 穿帮
class ChuanBang(models.Model):
    film = models.CharField(verbose_name='所属电影', max_length=255, default='')
    category = models.CharField(verbose_name='穿帮类型', max_length=255, default='')
    xiangqing = models.CharField(verbose_name='穿帮详情', max_length=255, default='')

    class Meta:
        verbose_name = '穿帮镜头'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name