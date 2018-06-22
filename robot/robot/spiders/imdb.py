# -*- coding: utf-8 -*-
import scrapy
import html2text
from film.models import Info as FilmInfo, Category as FilmCategory
from person.models import Info as PersonInfo

from extend.googletranslate import Translate


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/title/tt0371746/']
    # yiming = models.CharField(verbose_name='译名', max_length=255, null=True, blank=True)
    # jianjie = models.TextField(verbose_name='汉语简介', null=True, blank=True)  # 短
    # juqing = models.TextField(verbose_name='汉语剧情', null=True, blank=True)  # 长
    # ejianjie = models.TextField(verbose_name='英语简介', null=True, blank=True)  # 短
    # ejuqing = models.TextField(verbose_name='英语剧情', null=True, blank=True)  # 长
    # daoyan = models.CharField(verbose_name='导演', max_length=255, null=True, blank=True)
    # bianju = models.CharField(verbose_name='编剧', max_length=255, null=True, blank=True)
    # category = models.ManyToManyField(Category, verbose_name='类型')
    # yanyuan = models.ManyToManyField(PersonInfo, verbose_name='演员', null=True, blank=True)
    # chupingongsi = models.CharField(verbose_name='出品公司', max_length=255, null=True, blank=True)
    # zhipiangongsi = models.CharField(verbose_name='制片公司', max_length=255, null=True, blank=True)

    # zhipiandiqu = models.CharField(verbose_name='制片地区', max_length=255, null=True, blank=True)
    # chengben = models.CharField(verbose_name='制片成本', max_length=255, null=True, blank=True)
    # jibie = models.CharField(verbose_name='上映时间', max_length=255, null=True, blank=True)
    # paishedi = models.CharField(verbose_name='拍摄地点', max_length=255, null=True, blank=True)
    # duibai = models.CharField(verbose_name='对白语言', max_length=255, null=True, blank=True)
    # paisheriqi = models.CharField(verbose_name='拍摄日期', max_length=255, null=True, blank=True)
    # secai = models.CharField(verbose_name='色彩', max_length=255, null=True, blank=True)
    # imdb = models.CharField(verbose_name='IMDB编码', max_length=255, null=True, blank=True)

    # misuc = models.CharField(verbose_name='电影原声', max_length=255, null=True, blank=True)
    # db_fen = models.IntegerField(verbose_name='豆瓣评分', null=True, blank=True)

    # youku = models.TextField(verbose_name='优酷地址', null=True, blank=True)
    # bilibili = models.TextField(verbose_name='bilibili地址', null=True, blank=True)
    # aiqiyi = models.TextField(verbose_name='爱奇艺', null=True, blank=True)

    translate = Translate()

    def parse(self, response):
        ename = response.xpath('//h1/text()').extract_first()  # 英文名
        film = FilmInfo.objects.get(ename=ename)
        if film is None:  # 如果没有就加入电影
            film = FilmInfo.objects.create(ename=ename)

        name = self.translate.getResult(ename)  # 中文名
        imdb_fen = response.xpath('//span[@itemprop="ratingValue"]/text()').extract_first()  # imdb评分
        daoyan = response.xpath('//span[@itemprop="name"]/text()').extract_first()  # 导演
        year = response.xpath('//span[@id="titleYear"]/a/text()').extract_first()  # 年代
        jibie = response.xpath(
            '//div[@class="title_wrapper"]/div[@class="subtext"]/meta/@content').extract_first()  # 电影级别
        shichang = html2text.html2text(
            response.xpath('//div[@class="title_wrapper"]/div[@class="subtext"]/time/text()').extract_first())  # 时长
        category_list = response.xpath(
            '//div[@class="title_wrapper"]/div[@class="subtext"]/a[contains(@href,"genre")]/span/text()').extract()  # 电影类型【list】

        # 处理电影分类
        self.do_category(film.id, category_list)
        # 摘要+剧情;meta携带参数
        yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/plotsummary', callback=self.plotsummary,
                             meta={'film_id': film.id, 'category_list': category_list})

    def do_category(self, film_id, category_list):

        for category_name in category_list:
            # 翻译对应的电影分类名
            if category_name == 'Action':
                category_name = '动作'
            elif category_name == 'Adventure':
                category_name = '冒险'
            elif category_name == 'Sci-Fi':
                category_name = '科幻'
            # 如果电影分类中还没有这个分类就需要填加
            film_category = FilmCategory()
            category = film_category.objects.get(name=category_name)
            if category is None:
                category = film_category.objects.create(name=category_name)

            # 然后再填加这个电影的分类信息
            filminfo = FilmInfo()

    # 摘要+剧情
    def plotsummary(self,response):
        pass
