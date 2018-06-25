# -*- coding: utf-8 -*-
import scrapy
import html2text
from film import models as FM

from extend.googletranslate import Translate
from scrapy.selector import Selector


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/title/tt0371746/']

    # jianjie = models.TextField(verbose_name='汉语简介', default='')  # 短
    # juqing = models.TextField(verbose_name='汉语剧情', default='')  # 长
    # ejianjie = models.TextField(verbose_name='英语简介', default='')  # 短
    # ejuqing = models.TextField(verbose_name='英语剧情', default='')  # 长
    # jibie = models.TextField(verbose_name='电影级别', default='')

    # bianju = models.CharField(verbose_name='编剧', max_length=255, default='')
    # yanyuan = models.CharField(verbose_name='演员', max_length=255, default='')
    # guojia = models.CharField(verbose_name='国家', max_length=255, default='')

    # chupingongsi = models.CharField(verbose_name='出品公司', max_length=255, default='')
    # zhipiangongsi = models.CharField(verbose_name='制片公司', max_length=255, default='')
    # shichang = models.CharField(verbose_name='时长', max_length=255, default='')
    # zhipiandiqu = models.CharField(verbose_name='制片地区', max_length=255, default='')
    # chengben = models.CharField(verbose_name='制片成本', max_length=255, default='')
    # year = models.CharField(verbose_name='年代', max_length=255, default='')
    # paishedi = models.CharField(verbose_name='拍摄地点', max_length=255, default='')
    # duibai = models.CharField(verbose_name='对白语言', max_length=255, default='')
    # paisheriqi = models.CharField(verbose_name='拍摄日期', max_length=255, default='')
    # secai = models.CharField(verbose_name='色彩', max_length=255, default='')
    # imdb = models.CharField(verbose_name='IMDB编码', max_length=255, default='')
    # add_time = models.DateField(verbose_name='收录时间', default=datetime.now)
    # misuc = models.CharField(verbose_name='电影原声', max_length=255, default='')
    # db_fen = models.IntegerField(verbose_name='豆瓣评分', default=0)

    # youku = models.TextField(verbose_name='优酷地址', default='')
    # bilibili = models.TextField(verbose_name='bilibili地址', default='')
    # aiqiyi = models.TextField(verbose_name='爱奇艺', default='')

    translate = Translate()

    def parse(self, response):

        ename = response.xpath('//h1/text()').extract_first()  # 英文名
        name = self.translate.getResult(ename)  # 中文名

        imdb_fen = float(response.xpath('//span[@itemprop="ratingValue"]/text()').extract_first())  # imdb评分

        year = response.xpath('//span[@id="titleYear"]/a/text()').extract_first()  # 年代
        jibie = response.xpath(
            '//div[@class="title_wrapper"]/div[@class="subtext"]/meta/@content').extract_first()  # 电影级别
        shichang = html2text.html2text(
            response.xpath('//div[@class="title_wrapper"]/div[@class="subtext"]/time/text()').extract_first())  # 时长
        category_list = response.xpath(
            '//div[@class="title_wrapper"]/div[@class="subtext"]/a[contains(@href,"genre")]/span/text()').extract()  # 电影类型【list】
        # 处理电影分类
        category = self.trans_category(category_list)
        guojia = response.xpath(
            '//div[@id="titleDetails"]/div[@class="txt-block"]/a[contains(@href,"country")]/text()').extract_first()  # 国家/地区
        duibai_list = response.xpath(
            '//div[@id="titleDetails"]/div[@class="txt-block"]/a[contains(@href,"primary_language")]/text()').extract()  # 对白语言
        duibai = ','.join(duibai_list)
        # 如果已经存在会报错，需要处理
        FM.Info.objects.create(
            ename=ename,
            name=name,
            imdb_fen=imdb_fen,
            year=year,
            jibie=jibie,
            shichang=shichang,
            category=category,
            guojia=guojia,
            duibai=duibai,
        )
        # 摘要+剧情;meta携带参数
        # yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/plotsummary', callback=self.plotsummary,
        # meta={'film_name': name})
        # 导演+演员+编剧==
        # yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/fullcredits', callback=self.plotsummary,
        # meta={'film_name': name})

        # 译名+发布国家/日期--ok
        #yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/releaseinfo', callback=self.releaseinfo,
                             #meta={'film_name': name})

        ##整个制作团队（导演，编剧，演员……）
        yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/fullcredits', callback=self.fullcredits,
                             meta={'film_name': name})

    # 逐个翻译电影分类，返回一个带格式的字符串
    def trans_category(self, category_list):
        trans_list = []
        for category_name in category_list:
            # 翻译对应的电影分类名
            if category_name == 'Action':
                category_name = '动作'
            elif category_name == 'Adventure':
                category_name = '冒险'
            elif category_name == 'Sci-Fi':
                category_name = '科幻'
            trans_list.append(category_name)

        return ','.join(trans_list)

    # 摘要+剧情
    def plotsummary(self, response):
        pass

    # 译名+发布国家/日期
    def releaseinfo(self, response):
        film_name = response.meta['film_name']
        shangying_list = response.xpath('//table[@id="release_dates"]/tr').extract()
        # 国家/地区+上映日期+城市
        for li in shangying_list:
            '''
            '<tr class="odd">
            <td><a href="/calendar/?region=au&amp;ref_=ttrel_rel_1">Australia</a></td>
            <td class="release_date">14 April 2008</td>
            <td> (Sydney)
 (premiere)</td>
        </tr>'
            '''
            guojia = Selector(text=li).xpath('//td/a/text()').extract_first()
            shijian = Selector(text=li).xpath('//td[@class="release_date"]/text()').extract_first()
            chengshi = Selector(text=li).xpath('//td[last()]/text()').extract_first()
            FM.ShangYing.objects.create(
                film=film_name,
                guojia=guojia,
                chengshi=chengshi,
                shijian=shijian,
            )
            # 译名/别名
            yiming_list = response.xpath('//table[@id="akas"]/tr').extract()
            '''
            <tr class="odd">
                        <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">阿根廷</font></font></td>
                        <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">铁人 - 铁人</font></font></td>
                    </tr>
            '''
            for li in yiming_list:
                guojia = Selector(text=li).xpath('//td[last()-1]/text()').extract_first()
                yiming = Selector(text=li).xpath('//td[last()]/text()').extract_first()

                FM.YiMing.objects.create(
                    film=film_name,
                    guojia=guojia,
                    name=yiming,
                )

    # 整个制作团队（导演，编剧，演员……）
    def fullcredits(self):

        pass